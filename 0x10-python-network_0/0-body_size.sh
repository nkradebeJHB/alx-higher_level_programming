#!/bin/bash
# Bash script that takes in a URL, sends a 
# request to that URL, and displays the size 
# of the body of the response

curl -sI /dev/null | grep -i content-length | awk '{print $2}'
