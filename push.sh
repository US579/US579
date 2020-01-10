#!/bin/bash

msg=$@

git add .

if [ $# = 0 ]
then
    git commit -m  'commit'
else
    git commit -m "${msg}"
fi

git push
