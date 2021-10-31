#!/usr/bin/env python3

import time
import pigpio
import sys
import serialtest

I2C_ADDR=0x24
pi = pigpio.pi()
register = [None, None]

def i2c(id, tick):
   s, b, d = pi.bsc_i2c(I2C_ADDR)
   if b > 1:
       print("Received")
       register[d[0]] = bytearray([d[1]])
       #print(f"put {register[d[0]]} in reg")

   elif b == 1:
       print("Request to read")
       pi.bsc_i2c(I2C_ADDR, register[d[0]])

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
while serialtest.readBytes() != "stop":
    time.sleep(1)

serialtest.closeSerial()

e.cancel()

pi.bsc_i2c(0) # Disable BSC peripheral
pi.stop()
