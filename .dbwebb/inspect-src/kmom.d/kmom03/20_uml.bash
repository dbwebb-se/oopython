#!/usr/bin/env bash
cd me/$KMOM/war || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "View account_manager.py"
cat account_manager.py

read -p "Press to view accounts.py" answer
cat accounts.py

read -p "Press to view static/data/accounts.json" answer
cat static/data/accounts.json

read -p "Press to view app.py" answer
cat app.py