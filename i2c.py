#!/usr/bin/env python3

from os import read
from modules.Register import Register
from get_device_list import device_list
import time
import pigpio
import sys
import serialtest

I2C_ADDR=0x24
pi = pigpio.pi()
device = None

def i2c(id, tick):
   s, b, d = pi.bsc_i2c(I2C_ADDR)
   if b > 1:
       print("Received")
       device[d[0]].write(d[1])
       print("put {register[d[0]]} in reg")

   elif b == 1:
       print("Request to read")
       pi.bsc_i2c(I2C_ADDR, device[d[0]].data)

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
    time.sleep(1)
    data = serialtest.readBytes()

serialtest.closeSerial()

e.cancel()

pi.bsc_i2c(0) # Disable BSC peripheral
pi.stop()
