#!/usr/bin/env bash
s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME="$s"

export PYTHONPATH="$SCRIPT_HOME:$PYTHONPATH"

#                 #of worker  #show elapsed      #turn off warning
pipenv run pytest -n 2        --durations=0 -vv  --disable-pytest-warning
