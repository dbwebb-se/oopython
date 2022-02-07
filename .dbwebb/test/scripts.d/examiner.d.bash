#!/usr/bin/env bash
. "$COURSE_REPO_BASE/.dbwebb/test/functions.bash"

HEADER="scripts.d/$( basename -- "$0" ) start"
FOOTER="scripts.d/$( basename -- "$0" ) end"


printf "$HEADER

Unittests for $TESTSUITE:
$SEPARATOR

" | tee -a "$LOG"



DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TEST_TARGET=$(find "${DIR}/../suite.d" -name "${TESTSUITE}" -and -type d)
PATHS="$(find $TEST_TARGET -mindepth 1 -type d -and -not -name __pycache__)"

if [ "$PATHS" = "" ];
then
    if [[ -d "$TEST_TARGET" ]]
    then
        PATHS="$TEST_TARGET"
    fi
fi

status=0
for path_ in $PATHS; do
    bash -c "set -o pipefail && cd "${DIR}/.." && ${PYTHON_EXECUTER} -m ${EXAMINER_RUNNER} --what="${path_}" ${ARGUMENTS} 2>&1 | tee -a "$LOG" "
    status=$(($? + $status))
done;

printf "
$FOOTER
$SEPARATOR
" | tee -a "$LOG"

exit $status
