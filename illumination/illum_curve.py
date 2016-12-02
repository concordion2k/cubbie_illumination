import math
import time

pi = math.pi
counter = 0.0
bright = 0.0
increment = 0.1
amplitude = -0.5
wavelength = 2
xTransform = 0.8
yTransform = .5

# Illuminate LED...
while bright < .98:
        counter = counter + increment
        bright = (amplitude * math.sin(wavelength * (counter + xTransform))) + yTransform
        print "*" * int(bright * 100)
        print "Brightness: " + str(bright)
	print "Counter: " + str(counter)
	time.sleep(increment)

# Gradually dim / turn off LED...
while bright > 0:
        counter = counter - increment
        bright = (amplitude * math.sin(wavelength * (counter + xTransform))) + yTransform
        print "*" * int(bright * 100)
        print "Brightness: " + str(bright)
	print "Counter: " + str(counter)
	time.sleep(increment)
