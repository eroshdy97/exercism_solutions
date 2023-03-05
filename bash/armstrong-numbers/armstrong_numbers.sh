#!/usr/bin/env bash

power=${#1}
#echo "power = $power"
sum=0
for (( i=0; i<power; i++ )) ; do
    sum=$((sum + (${1:i:1} ** power)))
done
#echo "sum = $sum"
[ "$sum" -eq "$1" ] && echo true || echo false