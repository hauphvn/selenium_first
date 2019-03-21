#!/usr/bin/env bash
s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME="$s"

export PYTHONPATH="$SCRIPT_HOME:$PYTHONPATH"

#                 #of worker  #show elapsed      #turn off warning         #specific test to run
pipenv run pytest -n 2        --durations=0 -vv  --disable-pytest-warning  -k 'test_homepage' -s tests/test002.py