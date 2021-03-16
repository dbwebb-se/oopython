#!/usr/bin/env bash
cd me/$KMOM/lab4/ || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "This lab is optional, so it is very possible that the student is missing the lab."
read -p "Press to run answer.py" answer
python3 answer.py

read -p "Press to view answer.py" answer
cat answer.py
