#!/usr/bin/env bash

# Execute the student test files
# Only works when running test on kmom

HEADER="scripts.d/$( basename -- "$0" ) start"
FOOTER="scripts.d/$( basename -- "$0" ) end"
# takes name from dir name in suit.d/kmom0x/
# only works if there is one dir in suit.d/kmom0x/
ASSIGNMENT_NAME=$(ls $(find "${COURSE_REPO_BASE}/.dbwebb/test/suite.d" -name ${TESTSUITE} -and -type d))
ASSIGNMENT_PATH="$COURSE_REPO_BASE/me/$TESTSUITE/$ASSIGNMENT_NAME"

printf "$HEADER

Running test files in $ASSIGNMENT_NAME/tests
" | tee -a "$LOG"

bash -c "set -o pipefail && cd "$ASSIGNMENT_PATH" &&  ${PYTHON_EXECUTER} -m unittest discover tests""  2>&1  | tee -a "$LOG" "
status=$?

printf "
$FOOTER
$SEPARATOR
" | tee -a "$LOG"

exit $status