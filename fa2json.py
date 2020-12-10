#!/usr/bin/env python3

import sys
import json

def main():
    out = []
    header = ""
    seq = ""
    for l in sys.stdin:
        l = l.rstrip('\n')
        if len(l) <= 0:
            continue
        if l[0] == ">":
            if len(header) > 0 and len(seq) > 0:
                out.append({"header": header, "seq": seq})
            header = l[1:]
            seq = ""
        else:
            seq = seq + l
    if len(header) > 0 and len(seq) > 0:
        out.append({"header": header, "seq": seq})
    print(json.dumps(out, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
