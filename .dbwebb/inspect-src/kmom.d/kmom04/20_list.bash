#!/usr/bin/env bash
cd me/$KMOM/list || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

read -p "Press to run main.py" answer
python3 main.py

read -p "Press to view node.py" answer
cat node.py

read -p "Press to view unorderedlist.py" answer
cat unorderedlist.py

read -p "Press to view errors.py" answer
cat errors.py

read -p "Run test.py" answer
python3 -m unittest test.py

read -p "view test.py" answer
cat test.py