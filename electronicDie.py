
#https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/8
from sense_hat import SenseHat
import time

sense = SenseHat()

x, y, z = sense.get_accelerometer_raw().values()

x = abs(x)
y = abs(y)
z = abs(z)

def getdice():
	if x > 2 or y > 2 or z > 2:
        	sense.show_message("1")

count = 0
while True:
	getdice()
	time.sleep(10)
	count +1

	#x=round(x, 0)
	#y=round(y, 0)
	#z=round(z, 0)
	#print("x={0}, y={1}, z={2}".format(x, y, z))

	