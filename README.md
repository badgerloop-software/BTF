# BTF

A framework to unit test our device drivers.

## Setup
Ensure that the Beaglebone and the Pi are connected via the following interfaces:

- UART
    - RPi3
        - Tx: Pin 8
        - Rx: Pin 10
    - BBB
        - Tx: P9 Pin 13
        - Rx: P9 Pin 11
- I2C (Must be pulled up to 3.3V)
    - RPi3
        - SCL: Pin 35 (GPIO 19)
        - SDA: Pin 12 (GPIO 18)
    - BBB
        - SCL: P9 Pin 19
        - SDA: P9 Pin 20


## I2c testing

to run:
```console
sudo pigpiod
./i2c.py
```
to stop, pass any number of args:
```console
./i2c.py foo
```
