import pigpio

## Write functions to handle the following gpio cases

## Use pigpio library for interfacing with gpio pins
# https://abyz.me.uk/rpi/pigpio/python.html

## Case 1: 
# pin on BBB is set to 0 and 1 and needs to be validated by the Pi
def pi_read(pi):
    pi.set_mode(pinR, pigpio.INPUT)
    # pi reads BBB pin

    # pi outputs read value & caller verifies result
    # OR function compares BBB value and read value

## Case 2:
# pin on pi to be set to 0 and 1 by BBB and will be validated by the BBB
def pi_write(pi):
    pi.set_mode(pinW, pigpio.OUTPUT)

    # high test
    pi.write(pinW, high)
        #BBB checks gpio value
    
    #low test
    pi.write(pinW, low)
        #BBB checks gpio value