#include <stdio.h>
#include <stdbool.h>

void print_header(char *line, size_t entries_printed) {
    if (entries_printed > 0) {
        printf("\"\n        },\n");
    }
    printf("        {\n            \"header\": \"%s\",\n            \"seq\": \"", &line[1]);
}

void print_seq(char *line) {
    printf("%s", line);
}

void fq2json(FILE *inconn) {
    char *line = NULL;
    size_t len = 0;
    ssize_t nread;
    size_t entries_printed = 0;
    
    printf("{\n    \"entries\": [\n");
    while ((nread = getline(&line, &len, inconn)) != -1) {
        line[nread-1] = 0;
        if (nread > 1) {
            switch (line[0]) {
            case '>':
                print_header(line, entries_printed);
                entries_printed++;
                break;
            default:
                print_seq(line);
                break;
            }
        }
    }
    printf("\"\n        }\n    ]\n}\n");
}

int main() {
    fq2json(stdin);
    return(0);
}
