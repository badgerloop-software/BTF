from Register import Register

'''
Create definitions for mock devices 

Format:
deviceName = {
    "i2c_addr": 0x##,   // 7 bit address
    "registers": {
        0x00: Register(default value, size, writable),
        ...
        0x##: Register(default value, size, writable)
    }
    
}
'''

# Simple fake I2C device for BTF testing
mockDevice = {
    "i2c_addr": 0x11,
    "registers": {
        0x00: Register(0xFF, 8, False),
        0x01: Register(0x12, 8, True),
        0x02: Register(0x34, 8, False)
    }
    
}

# MCP23017 GPIO expander
mcp23017 = {
    "i2c_addr": 0x20,
    "registers": {
        0x00: Register(0xFF, 8, True),
        0x01: Register(0xFF, 8, True),
        0x12: Register(0x00, 8, True),     
        0x13: Register(0x00, 8, True)
    }
}

# TCA6416 GPIO expander
tca6416 = {
    "i2c_addr": 0x24,
    "registers": {
        0x00: Register(0xFF, 8, False),
        0x01: Register(0xFF, 8, False),
        0x02: Register(0xFF, 8, True),     
        0x03: Register(0xFF, 8, True),
        0x04: Register(0x00, 8, True),
        0x05: Register(0x00, 8, True),
        0x06: Register(0xFF, 8, True),     
        0x07: Register(0xFF, 8, True)
    }
}   

# Maps device name to appropriate register map
deviceList = {
    "mockDevice": mockDevice,
    "mcp23017": mcp23017,
    "tca6416": tca6416
}