#!/bin/bash

# Call this wrapper from anywhere to start a ep request. All arguments are forwarded to ep.py
# This wrapper will first initialize (or activate) a python environment with all needed packages.
# Intended usage is a convenient integration into external tools, e.g. IDEs.

clidir=$(dirname "$0")

if [ ! -d "$clidir/venv" ] 
then
    echo "First time use detected. Preparing python environment..."
    python3 -m venv ${clidir}/venv
    source ${clidir}/venv/bin/activate && pip3 install wheel && pip3 install -r ${clidir}/requirements.txt && echo "Environment prepared." && echo "." && echo "." 
fi

source $clidir/venv/bin/activate && python3 $clidir/ep.py "$@"