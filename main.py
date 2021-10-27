# Driver function for setting up simulated Devices
from modules.Register import Register

def main():
    # Create list of Devices
    device_0 = {
        0x00: Register(0xFF, 8, True),
        0x01: Register(0x52, 8, True),
        0x02: Register(0x00, 8, False),     
        0x03: Register(0x11, 8, False)
    }

    device_1 = {
        0x00: Register(0xFF, 8, True),
        0x01: Register(0x52, 8, True),
        0x02: Register(0x00, 8, False),     
        0x03: Register(0x11, 8, False)
    }

    # Can pass this device_list to wherever tests are ran
    device_list = {
        "d0": device_0,
        "d1": device_1
    }

    # Debug print all registers accessible from the device_list
    for device_name in device_list:
        for reg_address in device_list[device_name]:
            print(device_list[device_name][reg_address])


if __name__ == "__main__":
    main()
