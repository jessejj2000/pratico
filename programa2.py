import RPi.GPIO as GPIO
from time import sleep

# Configuração do modo de pinagem para BCM (Broadcom SOC channel)
GPIO.setmode (GPIO.BCM) 
GPIO.setwarnings(False)
# Seta o pino como output
GPIO.setup(23,GPIO.OUT)

#liga o led por 5s
GPIO.output(23,GPIO.HIGH)
sleep(5)


GPIO.output(23,GPIO.LOW)
