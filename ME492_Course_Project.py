#Kurtis Nemsky

import RPi.GPIO as GPIO
import time
from picamera import PiCamera

camera = PiCamera()
camera.rotation = 180
GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
LED_PIN = 18
GPIO.setup(PIR_PIN,GPIO.IN)
GPIO.setup(LED_PIN,GPIO.OUT)

i = 1

try:
	print("Motion Sensor Camera (Ctrl + C to exit)")
	time.sleep(2)
	print("Ready")
	while True:
		if GPIO.input(PIR_PIN):
			print("Motion Detected")
			GPIO.output(LED_PIN,True)
			time.sleep(2)
			camera.capture('/home/pi/Desktop/image%02d.jpg' % i)
			time.sleep(0.5)
			GPIO.output(LED_PIN,False)
		time.sleep(1)
		i = i + 1
except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
