#!/usr/bin/env bash
cd me/flask || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "View person.py"
cat person.py

read -p "Press to view app.py" answer
cat app.py
