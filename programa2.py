import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23,GPIO.OUT)

GPIO.output(23,GPIO.HIGH)
sleep(5)


GPIO.output(23,GPIO.LOW)
