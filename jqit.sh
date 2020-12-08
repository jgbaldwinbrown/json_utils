#!/bin/bash
set -e

./lsj.py | jq '.[].mode'
