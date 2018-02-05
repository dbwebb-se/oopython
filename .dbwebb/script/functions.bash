#!/usr/bin/env bash

#
# Error message and exit script.
# @arg1 string the message to display.
#
die()
{
    echo "$1";
    exit 1
}



#
# Read input from user supporting a default value for reponse.
# @arg1 string the message to display.
# @arg2 string the default value.
#
input()
{
    read -r -p "$1 [$2]: "
    echo "${REPLY:-$2}"
}



#
# Goto directory and check its status on .git
# @arg1 string the path to move to.
#
check_dir_for_git()
{
    pushd $1
    if [ ! -d .git ]; then
        echo "No git-repo on highest level: $1"
        ls -l
        return
    fi

    # Show details
    git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short
    echo "$1"
    git remote -v
    git tag

    # Checkout version and set it up
    TAG=$( input "Checkout tag" "" )
    git checkout $TAG
    npm install
    popd
}
