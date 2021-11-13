#!/bin/zsh

echo "Running all test cases from ./tests";
program=$1
tests=(tests/*[^.a])

for test in ${tests}
doE
    result=$(cat ${test} | ${program} | tr -d '[:space:]')
    expected=$(cat ${test}.a | tr -d '[:space:]')
    if [ ${result} = ${expected} ]
    then
        printf "Test %s OK\n" ${test}
    else
        printf "Test %s ERROR (actual:%s expected:%s)\n" ${test} ${result} ${expected}
    fi

doneEEg