#!/usr/bin/env bash
s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME="$s"

export PYTHONPATH="$SCRIPT_HOME:$PYTHONPATH"
pipenv run pytest