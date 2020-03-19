import json
from sense_hat import SenseHat
#https://pythonbasics.org/read-json-file/






with open('config.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

print("cold_max: " + str(obj['cold_max']))
print("comfortable_min: " + str(obj['comfortable_min']))
print("comfortable_max: " + str(obj['comfortable_max']))
