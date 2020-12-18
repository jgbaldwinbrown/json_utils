#!/usr/bin/env python3

import sys
import json
import argparse

def get_args():
    parser = argparse.ArgumentParser("Convert a table to JSON format")
    parser.add_argument("-n", "--no_header", help = "Do not take first row as header; instead, number entries.", action="store_true")
    parser.add_argument("-s", "--separator", help = "Column separator (default tab).", default = "\t")
    args = parser.parse_args()
    return(args)

def table2json(inconn, args):
    sep = args.separator
    header_names = []
    
    if not args.no_header:
        header_names = inconn.readline().rstrip('\n').split(sep)
    
    entries = []
    for line in inconn:
        entry = {}
        sline = line.rstrip('\n').split(sep)
        if not header_names:
            header_names = [str(x) for x in range(len(sline))]
        for name, value in zip(header_names, sline):
            entry[name] = value
        entries.append(entry)
    
    out = {}
    out["header"] = header_names
    out["entries"] = entries
    return(out)
        

def main():
    args = get_args()
    jtable = table2json(sys.stdin, args)
    print(json.dumps(jtable, indent=4))

if __name__ == "__main__":
    main()
