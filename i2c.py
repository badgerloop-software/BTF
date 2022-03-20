#!/usr/bin/env python3

from os import read
from modules.Register import Register
from get_device_list import get_device_list 
import time
import pigpio
import sys
import serialtest

I2C_ADDR=0x24
device_list = get_device_list();
pi = pigpio.pi()
device = device_list["ina3221"]

def i2c(id, tick):
   s, b, d = pi.bsc_i2c(I2C_ADDR)
   if b > 1:
       data = int.from_bytes(d[1:],"little")
       register = d[0]
       device[register].write(data)
       print(f"\nput {hex(data)} in reg {hex(register)}\nnew value: {hex(device[register].data)}\n")

   elif b == 1:
       print(f"Request to read register {hex(d[0])}")
       pi.bsc_i2c(I2C_ADDR, device[d[0]].data.to_bytes(device[d[0]].size//8,byteorder='little', signed=False))

if not pi.connected:
    exit()

if len(sys.argv) > 1:
    pi.bsc_i2c(0) # Disable BSC peripheral
    pi.stop()
    exit(0)

# Respond to BSC slave activity
e = pi.event_callback(pigpio.EVENT_BSC, i2c)
pi.bsc_i2c(I2C_ADDR) # Configure BSC as I2C slave

#serialtest.openSerial()
#data = serialtest.readBytes()
#while data != "stop":
#    if data in device_list:
#        device = device_list[data]
#    time.sleep(1)
#    data = serialtest.readBytes()
#
#serialtest.closeSerial()

time.sleep(36000)
e.cancel()

pi.bsc_i2c(0) # Disable BSC peripheral
pi.stop()
