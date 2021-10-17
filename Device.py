'''
This file represents a device that the Raspberry Pi will simulate.
'''
import Models.Register

class Device:
    name = "test device"
    # Mock register file
    # Key:   hexadecimal address to register
    # Value: Tuple ([data], [register size in bits])    
    reg_file = dict ({
        0 : (0xFF, 8),
        1 : (0x01, 8),
        2 : (0x03, 8),
        3 : (0x11, 8)
    })
