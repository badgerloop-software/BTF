# this file is a copy of serialtest.py from the old BTF repo. 
import serial
    
ser = serial.Serial()
ser.port = "/dev/serial0"
ser.baudrate = 9600

def openSerial():
    if not ser.is_open:
        ser.open()
        return ser.is_open

def readBytes():
    data = ser.readline()
    str = data.decode("utf-8")
    return str.strip()

def writeString(str):
    data = str.encode("utf-8")
    ser.write(data)

def closeSerial():
    ser.close()
    return ser.is_open