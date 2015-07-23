#!/usr/bin/env bash

methods="count bubble quick merge"
datasets="1k 2k 4k 8k 16k"

[[ $# > 0 ]] && { methods=$1 && shift; }
[[ $# > 0 ]] && { datasets="$@"; }

for m in $methods
do
    echo -e "\n###########################"
    echo -e "# Testing $m method"
    echo -e "###########################"
    for d in $datasets
    do
        echo -ne "- $m sort ($d): "
        read realtime result < <( ( time python methods/${m}.py testdata/${d}.txt ) 2>&1 | awk '
            /^real/ { real = $NF }
            /result:/ { result = $NF }
            END { print real, result }
            ' )
        echo "$result - $realtime"
    done
done
