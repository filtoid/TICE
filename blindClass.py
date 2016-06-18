import RPi.GPIO as GPIO
import time

class BlindClass(object):
	def __init__(self, pin1, pin2, pin3, pin4):
		self.sequence = [[1,0,0,1],
				 [1,0,0,0],
				 [1,1,0,0],
				 [0,1,0,0],
				 [0,1,1,0],
				 [0,0,1,0],
				 [0,0,1,1],
				 [0,0,0,1]]
		self.pins = [pin1, pin2, pin3, pin4]
		self.stepCount = 0
		GPIO.setup(pin1, GPIO.OUT)
		GPIO.setup(pin2, GPIO.OUT)
		GPIO.setup(pin3, GPIO.OUT)
		GPIO.setup(pin4, GPIO.OUT)

		GPIO.output(pin1, False)
		GPIO.output(pin2, False)
		GPIO.output(pin3, False)
		GPIO.output(pin4, False)
		 
		self.timer = 0 
		self.waitTime = 10/float(1000)
		self.MAX_TIMER = 10/self.waitTime
		self.state = 'closed'

	def _move(self, direction):
		for pin in range(0, len(self.pins)):
			xpin = self.pins[pin]
			if self.sequence[self.stepCount][pin] != 0:
				GPIO.output(xpin, True)
			else:
				GPIO.output(xpin, False)

		if direction == 'forward':
			self.stepCount += 1
		else:
			self.stepCount -= 1

		if self.stepCount > len(self.sequence)-1:
			self.stepCount = 0
		elif self.stepCount < 0: 
			self.stepCount = len(self.sequence)-1		


	def open(self):
		if self.state != 'closed':
			return

		self.timer = self.MAX_TIMER
		while self.timer > 0:
			self._move('forward')
			time.sleep(self.waitTime)
			self.timer -= 1

		self.state = 'open'	

	def close(self):
		if self.state != 'open':
			return

		self.timer = self.MAX_TIMER
		while self.timer > 0:
			self._move('backward')
			time.sleep(self.waitTime)
			self.timer -= 1		

		self.state = 'closed'

