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

res=""

if [[ $(($1 % 3)) -eq 0 ]]
then
    res+="Pling"
fi
if [[ $(($1 % 5)) -eq 0 ]]
then
    res+="Plang"
fi
if [[ $(($1 % 7)) -eq 0 ]]
then
    res+="Plong"
fi

if [[ $res == "" ]]
then
    echo "$1"
else
echo $res
fi
