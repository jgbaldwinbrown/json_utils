#!/usr/bin/env python3

import os
import json
import stat
import sys
from datetime import datetime
import argparse

def parse_my_args():
    parser = argparse.ArgumentParser("List directory entries in JSON format")
    parser.add_argument("path", help = "Path to directory to list", nargs = "?", default = "")
    parser.add_argument("-v", "--verbose", help = "Verbosely list all attributes of directory entries, not just human readable ones", required = False, action = "store_true")
    args = parser.parse_args()
    return(args)

def scan_it(dir_entries, verbose):
    out = []
    for entry in dir_entries:
        info = entry.stat()
        infodir = {}
        infodir["mtime"] = info.st_mtime
        infodir["size"] = info.st_size
        infodir["name"] = entry.name
        infodir["path"] = entry.path
        infodir["inode"] = entry.inode()
        infodir["is_dir"] = entry.is_dir()
        infodir["is_file"] = entry.is_file()
        infodir["is_symlink"] = entry.is_symlink()
        infodir["mode"] = stat.filemode(info.st_mode)
        infodir["last_modified"] = datetime.utcfromtimestamp(info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        if verbose:
            infodir["st_mode"] = info.st_mode
            infodir["st_ino"] = info.st_ino
            infodir["st_dev"] = info.st_dev
            infodir["st_nlink"] = info.st_nlink
            infodir["st_uid"] = info.st_uid
            infodir["st_gid"] = info.st_gid
            infodir["st_size"] = info.st_size
            infodir["st_atime"] = info.st_atime
            infodir["st_mtime"] = info.st_mtime
            infodir["st_ctime"] = info.st_ctime
            infodir["st_atime_ns"] = info.st_atime_ns
            infodir["st_mtime_ns"] = info.st_mtime_ns
            infodir["st_ctime_ns"] = info.st_ctime_ns

        out.append(infodir)
    return(out)

def walk_full_tree(root_dir, verbose):
    out = []
    for dir_name, sub_dir_list, file_list in os.walk(root_dir):
        out.extend(json_it(dir_name, verbose))
    return(out)

def json_it(path, verbose):
    if not path:
        with os.scandir() as dir_entries:
            out = scan_it(dir_entries, verbose)
    else:
        with os.scandir(path) as dir_entries:
            out = scan_it(dir_entries, verbose)
    return(out)

def json_print_tree(tree):
    print(json.dumps(tree, indent=4, sort_keys=True))

def main():
    args = parse_my_args()
    if args.path:
        tree = walk_full_tree(args.path, args.verbose)
    else:
        tree = walk_full_tree(".", args.verbose)
    json_print_tree(tree)

if __name__ == "__main__":
    main()

# import os, json; print json.dumps(os.listdir("."))
