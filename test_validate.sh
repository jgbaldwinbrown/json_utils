#!/bin/bash
set -e

cat test.fq | ./fq2json | python3 validate.py fqschema.json 
cat test.fa | ./fa2json | python3 validate.py fqschema.json 
cat test.fq | ./fq2json | python3 validate.py faschema.json 
