#!/usr/bin/env bash

seleniumContainers="docker ps -qa
                              -f name=selenium-hub
                              -f name=selenium-node-ch
                              -f name=selenium-node-ff
"
sh="docker rm -f \$($seleniumContainers)"
echo "$sh"
eval $sh

# docker rm -f \$(docker ps -qa) #remove all when needed
