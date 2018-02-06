#!/usr/bin/env bash
#
# Run this script, from the root of the course repo, to do a local inspect
# by downloading the files from the student server, start a non interactive
# local inspect through the Makefile and write all output to the file
# inspect.log.
#
# Script arguments:
#  $1 the kmom to inspect
#  $2 acronym to inspect
#  $3 empty, or something, to do potatoe for student acronym
#
# Usage:
#  .dbwebb/script/inspect-local.bash kmom01 abcd17
#  .dbwebb/script/inspect-local.bash kmom01 abcd17 p
#

# Include ./functions.bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source "$DIR/functions.bash"

# Get arguments
[[ $# == 2 || $# == 3 ]] ||
    die "Needs at least two arguments <kmom> <acronym> and optionally <potato>"

KMOM=$1
ACRONYM=$2

# Potatoe if needed
[ -z $3 ] || dbwebb run "sudo /usr/local/sbin/setpre-dbwebb-kurser.bash $ACRONYM"

# Download it
[ -d me ] || dbwebb init-me
dbwebb --yes --force download me $ACRONYM || exit 1

# Do local inspect
make inspect options="--yes" what=$KMOM > inspect.log
echo "Inspect done. Wrote output to inspect.log."
