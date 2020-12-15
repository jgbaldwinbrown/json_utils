#include <stdio.h>
#include <stdbool.h>

void fq2json(FILE *inconn) {
    char *line = NULL;
    size_t len = 0;
    ssize_t nread;
    size_t iter = 0;
    
    puts("{\n    \"entries\": [");
    while ((nread = getline(&line, &len, inconn)) != -1) {
        line[nread-1] = 0;
        switch (iter%4) {
        case 0:
            if (iter > 0) {
                puts(",");
            }
            printf("        {\n            \"header\": \"%s\",\n", &line[1]);
            break;
        case 1:
            printf("            \"seq\": \"%s\",\n", line);
            break;
        case 3:
            printf("            \"qual\": \"%s\"\n        }", line);
            break;
        default:
            break;
        }
        iter++;
    }
    puts("");
    puts("    ]\n}");
}

int main() {
    fq2json(stdin);
    return(0);
}
