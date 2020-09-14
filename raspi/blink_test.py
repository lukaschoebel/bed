#!/usr/bin/python
import time, sys
import RPi.GPIO as GPIO

redPin = 12   #Set to appropriate GPIO
greenPin = 19 #Should be set in the 
bluePin = 6  #GPIO.BOARD format

def turnOn(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def turnOff(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


def main():
    while True:
        cmd = raw_input("--> ")
        if cmd == "red on":
            redOn()
        elif cmd == "red off":
            redOff()
        elif cmd == "green on":
            greenOn()
        elif cmd == "green off":
            greenOff()
        elif cmd == "blue on":
            blueOn()
        elif cmd == "blue off":
            blueOff()
        elif cmd == "yellow on":
            yellowOn()
        elif cmd == "yellow off":
            yellowOff()
        elif cmd == "cyan on":
            cyanOn()
        elif cmd == "cyan off":
            cyanOff()
        elif cmd == "magenta on":
            magentaOn()
        elif cmd == "magenta off":
            magentaOff()
        elif cmd == "white on":
            whiteOn()
        elif cmd == "white off":
            whiteOff()
        else:
            print("Not a valid command")
    return

if __name__ == "__main__":
    print("+++ borki initialized +++")
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
    
