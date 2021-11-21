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

    # device_list can be passed to wherever tests are ran
    device_list = {
        "mcp23017": mcp23017
    }  
    
    return device_list


if __name__ == "__main__":
    device_list = get_device_list()
    # Debug print all registers accessible from the device_list
    for device_name in device_list:
        for reg_address in device_list[device_name]:
            print(device_list[device_name][reg_address])
