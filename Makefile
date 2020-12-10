all: fa2json fq2json

CC := gcc
CFLAGS := -O3 -Wall -Wextra -Wpedantic
LIBS := 

fa2json: fa2json.c
	$(CC) $(CFLAGS) -o $@ $< $(LIBS)

fq2json: fq2json.c
	$(CC) $(CFLAGS) -o $@ $< $(LIBS)
