# this file is a copy of serialtest.py from the old BTF repo. 
import serial
    
ser = serial.Serial()
ser.port = "/dev/ttyACM0"
ser.baudrate = 9600

def openSerial():
    if not ser.is_open:
        ser.open()
        return ser.is_open

def readBytes(timeout=0):
    origTimemout = ser.timeout
    if(timeout > 0):
        ser.timeout = timeout
    data = ser.readline()
    ser.timeout = origTimemout
    str = data.decode("utf-8")
    return str.strip()

def readAll(timeout=0):
    origTimeout = ser.timeout
    ser.timeout = 0 if timeout <= 0 else timeout
    data = ser.readlines()
    ser.timeout = origTimeout
    str = data.decode("utf-8")
    return str.strip()

def readUntil(str, size=None, timeout=0):
    origTimeout = ser.timeout
    ser.timeout = 0 if timeout <= 0 else timeout
    data = ser.read_until(str.encode("utf-8"), size)
    ser.timeout = origTimeout
    str = data.decode("utf-8")
    return str.strip()

def writeString(str):
    data = str.encode("utf-8")
    ser.write(data)

def closeSerial():
    ser.close()
    return ser.is_open
