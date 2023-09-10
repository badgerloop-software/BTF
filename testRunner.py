import sys
from i2cWrapper import i2c
import serialWrapper

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('You must specify the path to the config file as an argument')
        sys.exit(1)
    
    print(sys.argv[1])
    sys.exit(0)



# initialize Pi connection 
pi = pigpio.pi() 
if not pi.connected:
    exit()
# Respond to BSC slave activity (this event callback calls i2c())
e = pi.event_callback(pigpio.EVENT_BSC, i2c) 
# configure Pi as slave device 
pi.bsc_i2c(I2C_ADDR) 

# serial stuff
serialWrapper.openSerial()
data = serialWrapper.readBytes()
while data != "stop":
    time.sleep(1)
    data = serialtest.readBytes()


# turn everything off
e.cancel()
pi.bsc_i2c(0) # Disable BSC peripheral
pi.stop()
