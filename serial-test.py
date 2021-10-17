import serial

ser = serial.Serial("/dev/ttyS0")
#ser.port = "/dev/ttyS0"
#ser.baudrate = 115200

ser.open()
ser.is_open