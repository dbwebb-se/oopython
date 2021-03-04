#!/usr/bin/env bash
cd me/$KMOM/lab3/ || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

read -p "Press to run answer.py" answer
python3 answer.py

read -p "Press to view answer.py" answer
cat answer.py
