#!/usr/bin/env bash

sentence=${1,,}
alpha="abcdefghijklmnopqrstuvwxyz"

for (( i=0; i<26; i++)); do
    arr[i]=0
done

res=0
for (( i=0; i<${#sentence}; i++)); do
    pos=$(expr index "$alpha" "${sentence:i:1}")
    #echo "for i: $i ${sentence:i:1} pos = $pos and arr = ${arr[pos-1]}"
    if [[ ${arr[pos-1]} -eq 0 ]]; then
        arr[pos-1]=1
        res=$(( res + 1 ))
    fi
done
#echo "res = $res"
[[ "$res" = 26 ]] && echo true || echo false