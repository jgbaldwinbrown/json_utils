#!/usr/bin/env python3

import sys
import json

def add_qual_scores(fq):
    if "offset" in fq:
        offset = fq["offset"]
    else:
        offset = 33
    for entry in fq["entries"]:
        entry["qual_numeric_values"] = [ord(x) - offset for x in entry["qual"]]
    for entry in fq["entries"]:
        entry["error_probabilities"] = [10 ** (-x / 10) for x in entry["qual_numeric_values"]]

def main():
    fq = json.load(sys.stdin)
    add_qual_scores(fq)
    print(json.dumps(fq, indent=4))

if __name__ == "__main__":
    main()
