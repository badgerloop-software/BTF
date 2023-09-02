#!/bin/bash

usage="Usage: ./setup.sh </path/to/venv/>"

# Check if path for venv folder provided
if [[ -z "$1" ]]; then
    echo -e "Missing required argument.\n$usage\n"
    exit 1
fi
venv_path=$1

# Check if venv is installed, install if not
if [[ -z $(apt list --installed 2>/dev/null | grep python3-venv) ]]; then
    echo -e "Missing required package python3-venv. Please run \"sudo apt update && sudo apt install python3-venv\""
    exit 1
fi

# Create virtual environment at path
if [[ -z $(ls $venv_path 2>/dev/null)]]; then
    python3 -m venv $venv_path

    # Install dependencies
    source "$venv_path/bin/activate"
    pip -r "$(dirname "${BASH_SOURCE[0]}")/requirements.txt"

    deactivate
fi

