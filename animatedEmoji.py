from sense_hat import SenseHat

sense = SenseHat()

R = [255, 0, 0]# Red
G = [0, 255, 0]# Green
B = [0, 0, 255]# Blue
Y = [255, 255, 0]# Yellow
X = [0, 0, 0]# Black
W = [255, 255, 255]# White


question_mark = [
 W, W, W, R, R, W, W, W,
 W, W, R, W, W, R, W, W,
 W, W, W, W, W, R, W, W,
 W, W, W, W, R, W, W, W,
 W, W, W, R, W, W, W, W,
 W, W, W, R, W, W, W, W,
 W, W, W, W, W, W, W, W,
 R, W, W, R, W, W, W, W
]

sense.set_pixels(question_mark)

##https://pythonhosted.org/sense-hat/api/
