#!/usr/bin/env bash
cd me/$KMOM/queue || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "Run tests.py"
python3 -m unittest tests.py

read -p "Press to view node.py" answer
cat node.py

read -p "Press to view queue.py" answer
cat queue.py

read -p "Press to view errors.py" answer
cat errors.py

read -p "Press to run main.py" answer
python3 main.py

read -p "view tests.py" answer
cat tests.py
