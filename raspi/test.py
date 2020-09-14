#!/usr/bin/python3
import os
import time
from time import sleep
import RPi.GPIO as GPIO

BTN_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(BTN_PIN, GPIO.FALLING)
GPIO.setwarnings(False)


def sendData(infested):
    if infested:
        print("Tree infested!")
    else:
        print("Tree clean!")


if __name__ == "__main__":
    print("+++ borki69 intialized +++")
    while True:
        if GPIO.event_detected(BTN_PIN):
            print("detected")
            GPIO.remove_event_detect(BTN_PIN)
            now = time.time()
            count = 1
            GPIO.add_event_detect(BTN_PIN, GPIO.RISING)
            while time.time() < now + 1: # 1 second period
                if GPIO.event_detected(BTN_PIN):
                    count += 1
                    time.sleep(.05) # debounce time
            
            if count == 2:
                sendData(False) # single press
                GPIO.remove_event_detect(BTN_PIN)
                GPIO.add_event_detect(BTN_PIN, GPIO.FALLING)
            elif count == 3:
                sendData(True) # double press
                GPIO.remove_event_detect(BTN_PIN)
                GPIO.add_event_detect(BTN_PIN, GPIO.FALLING)
    GPIO.cleanup()
