#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

struct strlist {
    char **entries;
    size_t len;
    size_t cap;
};

struct strlist init_strlist(size_t cap) {
    struct strlist out;
    out.entries = calloc(cap, sizeof(char *));
    if (! out.entries) {
        fputs("out of memory!", stderr);
        exit(1);
    }
    out.len = 0;
    out.cap = cap;
    return(out);
}

void free_strlist(struct strlist list) {
    for (size_t i=0; i<list.len; i++) {
        free(list.entries[i]);
    }
}

void add_entry(char *entry, struct strlist *list) {
    if (list->len >= list->cap) {
        list->entries = realloc(list->entries, sizeof(char *) * list->cap * 2);
        if (! list->entries) {
            fputs("list of memory!", stderr);
            exit(1);
        }
        list->cap *= 2;
    }
    list->entries[list->len] = strdup(entry);
    list->len++;
}

struct strlist get_header_names(FILE *inconn) {
    struct strlist header_names = init_strlist(5);
    char *token = NULL;
    char *separator = "\t\n";
    char *line = NULL;
    size_t len = 0;
    ssize_t nread = 0;
    
    nread = getline(&line, &len, inconn);
    if (nread == -1) {
        fputs("no header line!", stderr);
        exit(2);
    }
    
    token = strtok(line, separator);
    
    while (token != NULL) {
        add_entry(token, &header_names);
        token = strtok(NULL, separator);
    }
    
    return(header_names);
    
    free(line);
}

void print_header(struct strlist header_names) {
    size_t i=0;
    for (i=0; i < header_names.len-1; i++) {
        printf("        %s,\n", header_names.entries[i]);
    }
    printf("        %s\n    ],\n    \"entries\": [", header_names.entries[header_names.len-1]);
}

void parse_entries(FILE *inconn, FILE *outconn, struct strlist header_names) {
    char *token = NULL;
    char *separator = "\t\n";
    char *line = NULL;
    size_t len = 0;
    ssize_t nread = 0;
    size_t line_number = 0;
    
    while ((nread = getline(&line, &len, inconn)) != -1) {
        size_t i=0;
        token = strtok(line, separator);
        
        if (line_number != 0) {
            printf(",");
        }
        printf("\n        {\n");
        
        while (token != NULL) {
            printf("            \"%s\": \"%s\"", header_names.entries[i], token);
            
            token = strtok(NULL, separator);
            if (token != NULL) {
                printf(",");
            }
            printf("\n");
            i++;
        }
        printf("\n        }");
        line_number++;
    }
    free(line);
}

void table2json(FILE *inconn, FILE *outconn) {
    printf("{\n    \"header\": [\n");
    struct strlist header_names = get_header_names(inconn);
    print_header(header_names);
    parse_entries(inconn, outconn, header_names);
    printf("\n    ]\n}\n");
    free_strlist(header_names);
}

int main() {
    table2json(stdin, stdout);
    return(0);
}
