from blindClass import BlindClass
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

bc = BlindClass(14,15,18,23)
bc.open()
bc.close()

