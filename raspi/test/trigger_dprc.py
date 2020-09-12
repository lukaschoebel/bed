#!/usr/bin/python
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

@DeprecationWarning
def button_callback(channel):
    t1 = time.time()

    while GPIO.input(channel) == 0:
        pass
    
    duration = time.time() - t1
    if duration > 0.8:
        print("long!")
    else: 
        print("short!")


if __name__ == "__main__":
    GPIO.add_event_detect(18, GPIO.FALLING, callback=button_callback, bouncetime=300)
    msg = input('Press enter to quit\n\n')

    GPIO.cleanup()