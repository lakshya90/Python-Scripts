#!/bin/bash
#Usage: $1 is inputfile and $2 is output file which is a sorted input file.
cat $1 | sort -u > $2
