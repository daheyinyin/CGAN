#!/bin/bash

set -e

# Simple log helper functions
info() { echo -e "\033[1;34m[INFO ][MxStream] $1\033[1;37m" ; }
warn() { echo >&2 -e "\033[1;31m[WARN ][MxStream] $1\033[1;37m" ; }

export PYTHONPATH=$PYTHONPATH:${MX_SDK_HOME}/python

python3.7 main.py 
exit 0
