#!/usr/bin/env python3

import sys
import json

def main():
    out = []
    header = ""
    seq = ""
    qual = ""
    for i, l in enumerate(sys.stdin):
        l = l.rstrip('\n')
        if i%4 == 0:
            header = l[1:]
        if i%4 == 1:
            seq = l
        if i%4 == 3:
            qual = l
            out.append({"header": header, "seq": seq, "qual": qual})
    print(json.dumps(out, indent=4))

if __name__ == "__main__":
    main()
