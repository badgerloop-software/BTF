# Badgerloop Testing Framework

## Setup
This repository is designed for and validated on a Raspberry Pi 4 running Ubuntu 22.04 Jammy Jellyfish. The Pi is expected to have the following packages:
- python3 (Should be included by default on Ubuntu 22.04)
- python3-venv (`sudo apt update && sudo apt install python3-venv`)
- pigpiod (install using instructions [here](https://abyz.me.uk/rpi/pigpio/download.html))

Additionally, you will need two configuration files to indicate what mocks are needed and provide any necessary setup information.

## Running Tests
1. Run the setup script to create/update the python environment and fetch all required packages: `source ./setup.sh </path/to/venv>`
2. Run the test script: `python3 testRunner.py </path/to/testConfig.yml> </path/to/setupConfig.yml>`
    - You will need two [configuration files](#writing-the-configuration-files) to tell the runner what devices to mock and how.

## Writing the Configuration Files
See the [embedded-mbed README](https://github.com/badgerloop-software/embedded-mbed#readme) for information about creating the necessary configuration files.
