import deviceSpecs
import pigpio


"""
Base class representing a mock I2C device
"""
class I2CTemplate:
    # Called to create class instance in 'with' block
    # deviceName: Name of devince in deviceSpecs map
    # pi: Instance of pigpio that is running for test
    def __enter__(self, deviceName, pi):
        # Store device details
        devDef = deviceSpecs.device_list[deviceName]
        self.address = devDef["i2c_addr"]
        self.registers = devDef["registers"]

        # Link to pigpio
        if not pi.connected:
            print("ERROR: pigpio not connected")
            return

        self.pi = pi
        self.event_callback = pi.event_callback(pigpio.EVENT_BSC, self.i2cHandler)
        pi.bsc_i2c(self.address)

        print("Initialized " + deviceName + " with address " + self.address)


    # Called on exit of 'with' block to clean up resources
    def __exit__(self):
        self.event_callback.cancel()
        self.pi.bsc_i2c(0)


    # Handles I2C write requests to mock
    # Override based on device functionality
    def i2cHandler(self, id, tick):
        # status: Data about current pigpio operations (not relevant)
        # count: number of bytes of data arriving in I2C line
        # data: bytes from I2C line
        status, count, data = self.pi.bsc_i2c(self.address)

        # Update register contents if write
        if count > 1:
            if count - 1 != self.registers[data[0]].size:
                raise IndexError('Write incorrect size:' + str(count - 1) + 'instead of' + str(self.registers[data[0]].size))
            self.registers[data[0]].write(data[1:])

        # Update register pointer for next read response
        self.pi.bsc_i2c(self.address, self.registers[data[0]].data.to_bytes(1, byteorder='big', signed=False))