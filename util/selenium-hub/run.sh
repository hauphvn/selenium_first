#!/usr/bin/env bash

#get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME="$s"

docker-compose -f "$SCRIPT_HOME/docker-compose.yml" \
               -p 'aa'  up \
               -d \
               --force-recreate --remove-orphans \
               --scale selenium-node-ch=1 \
               --scale selenium-node-ff=0
