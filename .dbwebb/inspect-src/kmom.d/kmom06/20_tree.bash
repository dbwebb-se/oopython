#!/usr/bin/env bash
cd me/$KMOM/tree || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

read -p "Run test.py" answer
python3 -m unittest test.py

read -p "check that student hasn't changed test.py" answer
cat test.py

read -p "Press to view node.py" answer
cat node.py

read -p "Press to view bst.py" answer
cat bst.py
