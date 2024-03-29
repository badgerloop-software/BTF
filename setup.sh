#!/bin/bash

usage="Usage: source ./setup.sh </path/to/venv/>"

# Ensure the script is being sourced
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo -e "Must source the script.\n\n$usage\n"
    exit 1
fi

# Check if path for venv folder provided
if [[ -z "$1" ]]; then
    echo -e "Missing required argument.\n\n$usage\n"
    return 1
fi
venv_path=$1

# Check if venv is installed, instruct to install if not
if [[ -z $(apt list --installed 2>/dev/null | grep python3-venv) ]]; then
    echo -e "Missing required package python3-venv. Please run \"sudo apt update && sudo apt install python3-venv\""
    return 1
fi

# Create virtual environment at specified path if one does not already exist there
python3 -m venv $venv_path

# Install dependencies
source $venv_path/bin/activate
pip install -r "$(dirname "${BASH_SOURCE[0]}")/requirements.txt"


echo -e "\nCurrently running in the virtual environment at ${venv_path}. This environment is set up for BTF usage.\n\nIf any Python packages need to be installed or updated, exit the virtual environment, update\nrequirements.txt accordingly, and rerun setup.sh.\n\nYou can exit this virtual environment by running \`deactivate\`"
