#!/usr/bin/env bash
cd me/kmom10/spellchecker || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f


read -p "Have you seen merge sort or tested it? Prss anything to continue" answer

read -p "Have you seen if frequency is used? Prss anything to continue" answer

read -p "Look at flask files? Prss anything to continue" answer

bash
# cat analyze_functions.py

