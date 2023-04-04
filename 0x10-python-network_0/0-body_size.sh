#!/bin/bash
# Curls request and display size of the body
curl -so /dev/null -w '%{size_download}\n' "$1"
