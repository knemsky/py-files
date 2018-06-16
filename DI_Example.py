import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_num = 23
GPIO.setup(pin_num,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
		if GPIO.input(pin_num) == False:
			print("Button Pressed")
			time.sleep(0.2)
