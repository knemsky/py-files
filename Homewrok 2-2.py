import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pin1 = 17
pin2 = 27
pin3 = 22
pin4 = 5
pin5 = 6
pin6 = 13
pin7 = 12

GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)

GPIO.setup(pin4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin5,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin6,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin7,GPIO.IN,pull_up_down=GPIO.PUD_UP)

if GPIO.input(pin4) == True:
    GPIO.output(pin1,GPIO.HIGH)
elif GPIO.input(pin5) == True:
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.HIGH)
elif GPIO.input(pin6) == True:
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.HIGH)
elif GPIO.input(pin7) == True:
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
