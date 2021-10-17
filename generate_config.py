# Creates a conf file to be read by ConfigParser module

from configparser import ConfigParser
from Models import Register

config_object = ConfigParser()

# List of device names that are stored in this config file
config_object["DEVICE_LIST"]: [
    'DEVICE_1',
    'DEVICE_2'
] 

# Mock register file
# Key:   hexadecimal address to register
# Value: Register instance with specified data
config_object["DEVICE_1"] = {
        0 : Register.Register(0xFF, 8, False),
        1 : (0x01, 8),
        2 : (0x03, 8),
        3 : (0x11, 8)
}

config_object["DEVICE_2"] = {
        0 : (0xFF, 8),
        1 : (0x01, 8),
        2 : (0x03, 8),
        3 : (0x11, 8)
}

# Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)
