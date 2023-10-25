import serial

"""
Wrapper to facilitate communication with Nucleo over USB (UART)
"""

ser = serial.Serial()
ser.port = "/dev/ttyACM0"   # File for USB port
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
