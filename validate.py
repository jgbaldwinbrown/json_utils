#!/usr/bin/env python3

import json
import jsonschema
import sys

def main():
    with open(sys.argv[1], "r") as inconn:
        schema = json.load(inconn)
    instance = json.load(sys.stdin)
    try:
        jsonschema.validate(instance = instance, schema = schema)
        print("OK")
    except ValidationError:
        print("Not OK")

if __name__ == "__main__":
    main()
