#!/usr/bin/env python3

from os import read
from modules.Register import Register
from get_device_list import get_device_list 
import time
import pigpio
import sys
import serialtest
import gpio

I2C_ADDR=0x24
device_list = get_device_list();
pi = pigpio.pi()
device = device_list["mcp23017"]

def i2c(id, tick):
   s, b, d = pi.bsc_i2c(I2C_ADDR)
   if b > 1:
       device[d[0]].write(d[1])
       print(f"\nput {hex(d[1])} in reg {hex(d[0])}\nnew value: {hex(device[d[0]].data)}\n")

   elif b == 1:
       print(f"Request to read register {hex(d[0])}")
       pi.bsc_i2c(I2C_ADDR, device[d[0]].data.to_bytes(1,byteorder='big', signed=False))
       print(device[d[0]].data.to_bytes(1,byteorder='big', signed=False))

if not pi.connected:
    exit()

if len(sys.argv) > 1:
    pi.bsc_i2c(0) # Disable BSC peripheral
    pi.stop()
    exit(0)

# Respond to BSC slave activity
e = pi.event_callback(pigpio.EVENT_BSC, i2c)
pi.bsc_i2c(I2C_ADDR) # Configure BSC as I2C slave

serialtest.openSerial()
data = serialtest.readBytes()
while data != "stop":
    if data in device_list:
        device = device_list[data]
    else:
        # gpio tests
        message = data.split()
        # split data into message components
        if message[0] == "gpio":
            level = int(message[2])                     # set level for tests
            # Case 1: pin on BBB is set to level and is validated by pi
            if message[1] == "r":
                if gpio.pi_read(pi, level):         # call pi_read with pi and expected level
                    serialtest.writeString("y")     # output pass/fail message based off results
                else:
                    serialtest.writeString("n")     # output pass/fail message based off results
            # Case 2: pin on pi set to level and is validated by BBB
            elif message[1] == "w":
                gpio.pi_write(pi, level)            # call pi_write with pi and level to be set
                if pi.read(gpio.pinW) == level:            # check if pi pin is set to correct levels 
                    serialtest.writeString("y")     # output pass/fail message based off results
                else:
                    serialtest.writeString("n")     # output pass/fail message based off results     
    time.sleep(1)
    data = serialtest.readBytes()

serialtest.closeSerial()

e.cancel()

pi.bsc_i2c(0) # Disable BSC peripheral
pi.stop()
