#!/usr/bin/env python3

import os
import json
import stat
import sys

def scan_it(dir_entries):
    out = []
    for entry in dir_entries:
        info = entry.stat()
        infodir = {}
        infodir["mtime"] = info.st_mtime
        infodir["size"] = info.st_size
        infodir["name"] = entry.name
        infodir["mode"] = stat.filemode(info.st_mode)
        out.append(infodir)
    return(out)

def json_it(path):
    if not path:
        with os.scandir() as dir_entries:
            out = scan_it(dir_entries)
    else:
        with os.scandir(path) as dir_entries:
            out = scan_it(dir_entries)
    
    print(json.dumps(out))

def main():
    if len(sys.argv) > 1:
        json_it(sys.argv[1])
    else:
        json_it("")

if __name__ == "__main__":
    main()

# import os, json; print json.dumps(os.listdir("."))
