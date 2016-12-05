

import math
import time

class illumination:
	pi = math.pi
        counter = 0.0
        bright = 0.0
        increment = 0.1
        amplitude = 0.5
        wavelength = -(pi/2)
        xTransform = 0.8
        yTransform = 0.5

	def turnOn(self):
		
		# Illuminate LED...
		while self.bright < 1:
        		self.counter = self.counter + self.increment
        		self.bright = (self.amplitude * math.sin(self.wavelength * (self.counter + self.xTransform))) + self.yTransform
        		print "b: " + format(self.bright, '.4f') + " | " + "c: " + format(self.counter, '.2f') + " | ",
			print "*" * int(self.bright * 100)
			print "|"
			time.sleep(self.increment)

	def turnOff(self):
	
		# Gradually dim / turn off LED...
		while self.bright > 0:
        		self.counter = self.counter - self.increment
        		self.bright = (self.amplitude * math.sin(self.wavelength * (self.counter + self.xTransform))) + self.yTransform
        		print "b: " + format(self.bright, '.4f') + " | " + "c: " + format(self.counter, '.2f') + " | ",
        		print "*" * int(self.bright * 100)
        		print "|"
			time.sleep(self.increment)
