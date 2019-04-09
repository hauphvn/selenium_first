#!/usr/bin/env bash
s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME="$s"

only_google_test=$1

export PYTHONPATH="$SCRIPT_HOME:$PYTHONPATH"
#
#if [[ ! -z "$only_google_test" ]]; then
#    # run only google test
    #                 #of worker  #show elapsed                     #turn off warning         #specific test to run
    pipenv run pytest -n 1       --durations=0 -vv                 --disable-pytest-warning  -k 'test_buy_product' -s tests/test004.py
                                  #TODO why this param hide print()
#    pipenv run pytest -n 2        --durations=0 -vv               -s tests/selenium_demo.py

#else
#    # run all tests
#    pipenv run pytest -n 2        --durations=0 -vv                 --disable-pytest-warning
#fi
