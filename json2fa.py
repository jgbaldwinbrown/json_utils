#!/usr/bin/env python3

import sys
import json

def main():
    fa = json.load(sys.stdin)
    for entry in fa["entries"]:
        print(">" + entry["header"])
        print(entry["seq"])

if __name__ == "__main__":
    main()
