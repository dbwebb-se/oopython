#!/usr/bin/env bash
cd me/kmom10/spellchecker || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "Run spellchecker"
python3 spellchecker.py

read -p "Press to view node.py" answer
cat node.py


read -p "Press to view trie.py" answer
cat trie.py


read -p "Press to view spellchecker.py" answer
cat spellchecker.py



read -p "Press to run test.py" answer
python3 test.py

read -p "Press to view test.py" answer
cat test.py
