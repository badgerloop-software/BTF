import pigpio
from getDeviceList import get_device_list 

# setup macros and variables
I2C_ADDR = 0x24 # I2C address of this device
device_list = get_device_list() # the list of devices to test
device = device_list["mockDevice"] # select the device to test

# function which allows the I2C lines to access the device list
def i2c(id, tick):
    # status: (not important)
    # count: number of bytes of data arriving in I2C line
    # data: bytes from I2C line
    status, count, data = pi.bsc_i2c(I2C_ADDR)
    
    # write data to a register 
    if count > 1:
        device[data[0]].write(data[1])
        print(f"\nput {hex(data[1])} in reg {hex(data[0])}\nnew value: {hex(device[data[0]].data)}\n")
    # read a register
    elif count == 1:
        print(f"Request to read register {hex(data[0])}")
        pi.bsc_i2c(I2C_ADDR, device[data[0]].data.to_bytes(1,byteorder='big', signed=False))
        print(device[data[0]].data.to_bytes(1,byteorder='big', signed=False))