#!/bin/bash
set -e

./findj.py | ./sortj.py 'x["path"]' | jq '.[] | {inode, name}'
