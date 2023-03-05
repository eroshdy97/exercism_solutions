#!/usr/bin/env bash

# The following comments should help you get started:
# - Bash is flexible. You may use functions or write a "raw" script.
#
# - Complex code can be made easier to read by breaking it up
#   into functions, however this is sometimes overkill in bash.
#
# - You can find links about good style and other resources
#   for Bash in './README.md'. It came with this exercise.
#
#   Example:
#   # other functions here
#   # ...
#   # ...
#
#   main () {
#     # your main function code here
#   }
#
#   # call main with all of the positional arguments
#   main "$@"
#
# *** PLEASE REMOVE THESE COMMENTS BEFORE SUBMITTING YOUR SOLUTION ***
if [[ $# -lt 2 ]]
then
    echo "Usage: hamming.sh <string1> <string2>"
    exit 1
fi
ans=0
len1=${#1}
len2=${#2}

if [ "$len1" -eq "$len2" ]
then
    for i in $(seq 0 "$len2");
    do
        if [ "${1:$i:1}" != "${2:$i:1}" ]
        then
            #echo "FL: ${1:$i:1} SL: ${2:$i:1}"
            ans=$((ans+1))
        fi
    done
    echo $ans
else
    echo "strands must be of equal length"
    exit 1
fi

