import serial
    
ser = serial.Serial()
ser.port = "/dev/serial0"
ser.baudrate = 9600

def openSerial():
    if not ser.is_open:
        ser.open()
        return ser.is_open

def readBytes():
    ser.reset_input_buffer()
    while ser.in_waiting == 0:
        pass
    data = ser.read(ser.in_waiting)
    #print(data)
    str = data.decode("utf-8")
    #print(str)
    return str.strip()

def closeSerial():
    ser.close()
    return ser.is_open()

#print(ser.is_open)
