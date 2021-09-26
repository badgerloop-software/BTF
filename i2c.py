#!/usr/bin/env python3

import time
import pigpio

I2C_ADDR=0x21
pi = pigpio.pi()

def i2c(id, tick):
   s, b, d = pi.bsc_i2c(I2C_ADDR)

   if b:
      print("-"*20)
      print(f"status: {s}")
      print(f"num bytes read: {b}")
      print(f"byte array: {d.hex()}")
      print("-"*20)
      

if not pi.connected:
    exit()

# Respond to BSC slave activity

e = pi.event_callback(pigpio.EVENT_BSC, i2c)
pi.bsc_i2c(I2C_ADDR) # Configure BSC as I2C slave

time.sleep(600)
e.cancel()

pi.bsc_i2c(0) # Disable BSC peripheral
pi.stop()
