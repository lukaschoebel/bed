#!/usr/bin/python3
import os
import time
from time import sleep
import RPi.GPIO as GPIO

sw_in = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(sw_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(sw_in, GPIO.FALLING)
GPIO.setwarnings(False)

def sendData(infested):
    if infested:
        print("Tree infested!")
    else:
        print("Tree clean!")


if __name__ == "__main__":
    print("intialized")
    while True:
        if GPIO.event_detected(sw_in):
            print("detected")
            GPIO.remove_event_detect(sw_in)
            now = time.time()
            count = 1
            GPIO.add_event_detect(sw_in, GPIO.RISING)
            while time.time() < now + 1: # 1 second period
                if GPIO.event_detected(sw_in):
                    count += 1
                    time.sleep(.25) # debounce time
            #print count
            #performing required task!
            if count == 2:
                sendData(False) # single press
                GPIO.remove_event_detect(sw_in)
                GPIO.add_event_detect(sw_in, GPIO.FALLING)
            elif count == 3:
                sendData(True) # double press
                GPIO.remove_event_detect(sw_in)
                GPIO.add_event_detect(sw_in, GPIO.FALLING)
    GPIO.cleanup()
