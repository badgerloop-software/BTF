import serial

ser = serial.Serial()
ser.port = "/dev/ttyS0"
ser.baudrate = 115200

if not ser.is_open:
    ser.open()

data = ser.read(8)
print(data)

ser.close()
print(ser.is_open)
