#!/usr/bin/env python3

import sys
import json

def main():
    fq = json.load(sys.stdin)
    for entry in fq["entries"]:
        entry["len"] = len(entry["seq"])
    print(json.dumps(fq, indent=4))

if __name__ == "__main__":
    main()
