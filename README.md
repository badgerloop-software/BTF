# Badgerloop Testing Framework

## Setup
This repository is designed for and validated on a Raspberry Pi 4 running Ubuntu 22.04 Jammy Jellyfish. The Pi is expected to have the following packages:
- python3 (Should be included by default on Ubuntu 22.04)
- python3-venv (sudo apt update && sudo apt install python3-venv)
- pigpiod (sudo apt update && sudo apt install pigpiod)

Additionally, you will need a testConfig file to indicate what mocks are needed. 

## Running Tests
1. Run the setup script to create the python environment and fetch all required packages (./setup.sh </folder/to/create/in>)
2. Activate the python environment (source </folder/you/specified/above>)
3. Run the test script. You will need a [configuration file](#writing-the-configuration-file) to tell the runner what devices to mock and how. (python3 testRunner.py </path/to/testConfig/file>)


## Writing the Configuration File
TBD