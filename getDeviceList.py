from Register import Register

def get_device_list():
    """Forms a device list in which devices can be indexed by the device's name.
        
        Returns: A list of mock devices to use for testing
    """
    # Create devices
    mockDevice = {
        "i2c_addr": 0x11,
        0x00: Register(0xFF, 8, False),
        0x01: Register(0x12, 8, True),
        0x02: Register(0x34, 8, False)
    }

    mcp23017 = {
        "i2c_addr": 0x20,
        0x00: Register(0xFF, 8, True),
        0x01: Register(0xFF, 8, True),
        0x12: Register(0x00, 8, True),     
        0x13: Register(0x00, 8, True)
    }

    tca6416 = {
        "i2c_addr": 0x24,
        0x00: Register(0xFF, 8, False),
        0x01: Register(0xFF, 8, False),
        0x02: Register(0xFF, 8, True),     
        0x03: Register(0xFF, 8, True),
        0x04: Register(0x00, 8, True),
        0x05: Register(0x00, 8, True),
        0x06: Register(0xFF, 8, True),     
        0x07: Register(0xFF, 8, True),
    }

    # device_list can be passed to wherever tests are ran
    device_list = {
        "mockDevice": mockDevice,
        "mcp23017": mcp23017,
        "tca6416": tca6416
    }

    # Debug print all registers accessible from the device_list
    for device_name in device_list:
        for reg_address in device_list[device_name]:
            print(device_list[device_name][reg_address])
    
    return device_list


if __name__ == "__main__":
    get_device_list()
