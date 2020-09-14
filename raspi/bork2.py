#!/usr/bin/python3
import RPi.GPIO as GPIO
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class ButtonHandler(threading.Thread):
    def __init__(self, pin, func, edge='both', bouncetime=200):
        super().__init__(daemon=True)

        self.edge = edge
        self.func = func
        self.pin = pin
        self.bouncetime = float(bouncetime)/1000

        self.lastpinval = GPIO.input(self.pin)
        self.lock = threading.Lock()

    def __call__(self, *args):
        if not self.lock.acquire(blocking=False):
            return

        t = threading.Timer(self.bouncetime, self.read, args=args)
        t.start()

    def read(self, *args):
        pinval = GPIO.input(self.pin)

        if (
                ((pinval == 0 and self.lastpinval == 1) and
                 (self.edge in ['falling', 'both'])) or
                ((pinval == 1 and self.lastpinval == 0) and
                 (self.edge in ['rising', 'both']))
        ):
            self.func(*args)

        self.lastpinval = pinval
        self.lock.release()


def real_cb(PIN):
    val = GPIO.input(PIN)
    print("detected " + val) 
    # val = GPIO.input(pin)
    # if val == 1:
    #     print("detected") 


if __name__ == "__main__":
    cb = ButtonHandler(18, real_cb, edge='rising', bouncetime=100)
    cb.start()

    try:
        while True:
            GPIO.add_event_detect(18, GPIO.RISING, callback=cb)
    except KeyboardInterrupt:
        GPIO.cleanup()