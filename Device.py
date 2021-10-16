# This file represents a device that the Raspberry Pi will simulate.
# Instance Fields:
#   SCP (serial communication protocol)
#
# Instance Functions:
#   Input(): Read from registers
#
#   Output(): Write to registers

# TODO Implement
import Models.Register

class Device:
    name = "test device"
    # Mock register file
    # Key:   hexadecimal address to register
    # Value: Tuple ([data], [register size in bits])    
    reg_file = dict ({
        '0x0000' : ('00000000', '8'),
        '0x0001' : ('00000001', '8'),
        '0x0002' : ('00000011', '8'),
        '0x0003' : ('00000100', '8')
    })
