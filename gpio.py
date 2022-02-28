import pigpio

# Define pins
pinR = 23
pinW = 24

## Write functions to handle the following gpio cases

## Use pigpio library for interfacing with gpio pins
# https://abyz.me.uk/rpi/pigpio/python.html

## Case 1: 
# pin on BBB is set to 0 and 1 and needs to be validated by the Pi
def pi_read(pi, expected):
    pi.set_mode(pinR, pigpio.INPUT)
    # return if read value matches expected
    return(pi.read(pinR) == expected)

## Case 2:
# pin on pi to be set to 0 and 1 by BBB and will be validated by the BBB
def pi_write(pi, level):
    pi.set_mode(pinW, pigpio.OUTPUT)
    pi.write(pinW, level)   # set level
