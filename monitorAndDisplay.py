import json
import time
from sense_hat import SenseHat
#https://pythonbasics.org/read-json-file/

#JSON read
with open('config.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

#JSON test print
print("cold_max: " + str(obj['cold_max']))
print("comfortable_min: " + str(obj['comfortable_min']))
print("comfortable_max: " + str(obj['comfortable_max']))


def temp():
	sense.show_message("test")
#       time.sleep(5)
#	sense.show_message("Temp: %s C" % temp)
#	print("Temperature: %s C" % temp)
#	print(sense.temp)



sense = SenseHat()
temp = sense.get_temperature()
print("Temperature: %s C" % temp)
