# Driver function for testing stuff
from configparser import ConfigParser
import json


if __name__ == "__main__":
    #Read config.ini file
    config_object = ConfigParser()
    config_object.read("config.ini")

    # Grab device list   
    device_list = config_object.get("DEVICE_LIST", "value")
    # TODO This only sees device_list as a string. Is using ConfigParser necessary?
    print(device_list)
