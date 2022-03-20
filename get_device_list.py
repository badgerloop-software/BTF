from modules.Register import Register

def get_device_list():
    """Forms a device list in which devices can be indexed by the device's name.
        
        Returns: A list of mock devices to use for testing
    """
    # Create devices
    mcp23017 = {
        0x00: Register(0xFF, 8, True),
        0x01: Register(0xFF, 8, True),
        0x12: Register(0x00, 8, True),     
        0x13: Register(0x00, 8, True)
    }

    # Only using registers 0-6, ID registers FE and FF. 
    # Register values are POWER-ON RESET values from Table 3 of datasheet.
    ina3221 = {
        0x00: Register(0x7127, 16, True),
        0x01: Register(0x0000, 16, False),
        0x02: Register(0x0000, 16, False),
        0x03: Register(0x0000, 16, False),
        0x04: Register(0x0000, 16, False),
        0x05: Register(0x0000, 16, False),
        0x06: Register(0x0000, 16, False),
        0x07: Register(0x0000, 16, True),
        0x08: Register(0x0000, 16, True),
        0x09: Register(0x0000, 16, True),
        0x0A: Register(0x0000, 16, True),
        0x0B: Register(0x0000, 16, True),
        0x0C: Register(0x0000, 16, True),
        0x10: Register(0x0000, 16, True),
        0x11: Register(0x0000, 16, True),
        0xFE: Register(0x5449, 16, False),
        0xFF: Register(0x3220, 16, False)
    }

    # device_list can be passed to wherever tests are ran
    device_list = {
        "mcp23017": mcp23017,
        "ina3221": ina3221
    }  

    return device_list


if __name__ == "__main__":
    device_list = get_device_list()
    # Debug print all registers accessible from the device_list
    for device_name in device_list:
        print(f"---------\n{device_name}\n---------\n")
        for reg_address in device_list[device_name]:
            print(f"Register {hex(reg_address)}\n-------------\n{device_list[device_name][reg_address]}")
