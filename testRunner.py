from mocks.I2CTemplate import I2CTemplate
import interfaces.serialWrapper as serialWrapper
import pigpio
import time


print('Initializing pi')

# initialize Pi connection 
pi = pigpio.pi() 
if not pi.connected:
    exit()


try:
	print('Creating mock')
	with I2CTemplate('mockDevice', pi) as mockDevice:
		print('Opening serial')
		# set up serial to receive test commands from Nucleo
		serialWrapper.openSerial()

		print('Running tests')
		data = serialWrapper.readBytes()
		# keep running until "stop" message is received
		while data != "stop":
			print(data)
			time.sleep(1)
			data = serialWrapper.readBytes()

		print("tests done")
except Exception as e:
	print(e)


# turn everything off
pi.stop()
