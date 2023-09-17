import pigpio
from getDeviceList import get_device_list 

# setup macros and variables
device_list = get_device_list() # the list of devices to test
device = device_list["mockDevice"] # select default device to test
I2C_ADDR = device["i2c_addr"] # default I2C address

# function to change the i2c device this wrapper is modeling
# d the name of the device 
# returns True if the input name was a valid device, False otherwise
def changeDevice(d):
    if d in device_list:
        device = device_list[d]
        I2C_ADDR = device["i2c_addr"]
        return True
    else:
        return False


# function which allows the I2C lines to access the device
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
        pi.bsc_i2c(I2C_ADDR, device[data[0]].data.to_bytes(1, byteorder='big', signed=False))
        print(device[data[0]].data.to_bytes(1, byteorder='big', signed=False))