#!/bin/bash
#Usage: $1 is file1, $2 is file2, $3 is overlap between file 1 and file 2
comm -12 $1 $2 > $3
