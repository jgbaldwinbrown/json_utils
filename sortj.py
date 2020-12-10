#!/usr/bin/env python3

import sys
import json

def main():
    indata = json.load(sys.stdin)
    sort_text = sys.argv[1]
    sort_func_text = "lambda x: " + sort_text
    sort_func = eval(sort_func_text)
    out = sorted(indata, key = sort_func)
    print(json.dumps(out, indent=4))

if __name__ == "__main__":
    main()
