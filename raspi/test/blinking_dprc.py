#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)

@DeprecationWarning
if __name__ == "__main__":
  while True:
    print("LED on")
    GPIO.output(19,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(19,GPIO.LOW)
    time.sleep(1)