import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #broadcom
#GPIO.setmode(GPIO.BOARD)

LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)  

try:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(2) 

    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(2)

    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(2)

finally:
    GPIO.cleanup()

