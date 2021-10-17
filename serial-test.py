import serial

ser = serial.Serial()
ser.port = "/dev/ttyS0"
ser.baudrate = 115200

if not ser.is_open:
    ser.open()

ser.read(8)

ser.close()
