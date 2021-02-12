#!/usr/bin/env bash
cd me/$KMOM/bank2 || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "View account_manager.py"
cat account_manager.py

read -p "Press to view accounts.py" answer
cat accounts.py

read -p "Press to view person.py" answer
cat person.py

read -p "Press to view static/data/accounts.json" answer
cat static/data/accounts.json

read -p "Run tests.py" answer
python3 -m unittest tests.py

read -p "view tests.py" answer
cat tests.py

read -p "Press to view app.py" answer
cat app.py