#!/usr/bin/env bash

# Execute the student test files
# Only works when running test on kmom

HEADER="scripts.d/$( basename -- "$0" ) start"
FOOTER="scripts.d/$( basename -- "$0" ) end"


contains_name() {
    # check if part of a path is equal to assignmen name
    local counter=0
    for i in ${path_pars[@]}
    do
        if [[ "$i" == "$name" ]]; then
            echo "1"
            return
        fi
    done

    echo "0"
    return
}

DBWEBB_MAP="$COURSE_REPO_BASE/.dbwebb.map"
map_paths_array="$(cat $DBWEBB_MAP | awk "/[\/]$TESTSUITE/")"

# takes name from dir name in suit.d/kmom0x/
ASSIGNMENT_NAMES="$(ls $(find "${COURSE_REPO_BASE}/.dbwebb/test/suite.d" -name ${TESTSUITE} -and -type d))"

# match part of mapp path with assignment name to find assignment path
for name in $ASSIGNMENT_NAMES; do
    for path in $map_paths_array; do
        path_pars=(${path//\// })
        res="$(contains_name)"
        if [[ $res == "1" ]]; then
            printf "$HEADER

Running test files in $path/tests
" | tee -a "$LOG"

            ASSIGNMENT_PATH="$COURSE_REPO_BASE/$path"
            bash -c "set -o pipefail && cd "$ASSIGNMENT_PATH" &&  ${PYTHON_EXECUTER} -m unittest discover tests""  2>&1  | tee -a "$LOG" "
            status=$?
        fi

    done;
done;


printf "
$FOOTER
$SEPARATOR
" | tee -a "$LOG"

exit $status