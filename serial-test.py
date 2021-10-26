import serial

ser = serial.Serial()
ser.port = "/dev/serial0"
ser.baudrate = 9600

if not ser.is_open:
    ser.open()
ser.reset_input_buffer()

data = ser.read(8)
print(data)

str = data.decode("utf-8")
print (str)

ser.close()
print(ser.is_open)
