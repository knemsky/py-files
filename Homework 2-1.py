import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin1 = 17
pin2 = 27
pin3 = 22

GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)

user = int(input("Please enter a number between 1 and 3: "))

if user == 1:
    GPIO.output(pin1,GPIO.HIGH)
elif user == 2:
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.HIGH)
elif user == 3:
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.HIGH)
else:
    print("Error: Not a valid input")