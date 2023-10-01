import sys
from getDeviceList import get_device_list
import interfaces.serialWrapper as serialWrapper
import pigpio
import time


#if __name__ == '__main__':
#    if len(sys.argv) != 2:
#        print('You must specify the path to the config file as an argument')
#        sys.exit(1)
    
#    print(sys.argv[1])
#    sys.exit(0)

device_list = get_device_list()
device = device_list["mockDevice"]
I2C_ADDR = device["i2c_addr"]


# function which allows the I2C lines to access the device
def i2c(id, tick):
	global pi
	print("i2c method called")
	# status: (not important)
	# count: number of bytes of data arriving in I2C line
	# data: bytes from I2C line
	status, count, data = pi.bsc_i2c(I2C_ADDR)
    
	# write data to a register 
	if count > 1:
		print(f"\nput {hex(data[1])} in reg {hex(data[0])}\nnew value: {hex(device[data[0]].data)}\n")
		device[data[0]].write(data[1])
	# read a register
	elif count == 1:
		print(f"Request to read register {hex(data[0])}")
		pi.bsc_i2c(I2C_ADDR, device[data[0]].data.to_bytes(1, byteorder='big', signed=False))
		print(device[data[0]].data.to_bytes(1, byteorder='big', signed=False))

# initialize Pi connection 
pi = pigpio.pi() 
if not pi.connected:
    exit()

# Respond to BSC slave activity (this event callback calls i2c())
e = pi.event_callback(pigpio.EVENT_BSC, i2c)

# configure Pi as slave device 
pi.bsc_i2c(I2C_ADDR)

print("mockDevice address:")
print(str(I2C_ADDR))

# set up serial to receive test commands from Nucleo
serialWrapper.openSerial()
data = serialWrapper.readBytes()
# keep running until "stop" message is received
while data != "stop":
	print(data)
	time.sleep(1)
	data = serialWrapper.readBytes()

print("tests done")

# turn everything off
e.cancel()
pi.bsc_i2c(0) # Disable BSC peripheral
pi.stop()
