#!/bin/bash

read Q
read N
read -a D
read -a P

sorted_D=$(for x in "${D[@]}"; do echo $x; done | sort -nr)

if [ "$Q" -eq 1 ]; then
	sorted_P=$(for x in "${P[@]}"; do echo $x; done | sort -nr)
elif [ "$Q" -eq 2 ]; then
	sorted_P=$(for x in "${P[@]}"; do echo $x; done | sort -n)
fi
totalSpeed=0
for i in $(seq 0 $(((N-1))); do
	d=${sorted_D[$i]}
	p=${sorted_P[$i]}
	if [ "$d" -gt "$p" ]; then
		total=$(expr $total + $d)
	else
		total=$(expr $total + $p)
	fi
done
echo totalSpeed
