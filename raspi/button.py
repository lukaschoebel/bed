#!/usr/bin/python
import time
import random
import threading
import firebase_admin
import RPi.GPIO as GPIO
from firebase_admin import credentials, firestore

cred = credentials.Certificate("secrets/firestore-creds.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# reference to the firestore document
doc_ref = db.collection(u'current_measure').document(u'0')

RED = 12
GREEN = 19
BLUE = 6
BUTTON_1 = 17
BUTTON_2 = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # button 1
GPIO.setup(BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # button 2

count = 0
prev_inp = 1

def turnOn(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def turnOff(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def measure_light(n_times):
    """
    Blue blinking measurement lights

    Args:
        n_times (int): Specifies the count of measure blinks
    """

    for _ in range(n_times):
        turnOn(BLUE)
        time.sleep(0.5)
        turnOff(BLUE)
        time.sleep(0.5)
    time.sleep(0.5)

def blink(pin):
    time.sleep(0.15)
    measure_light(6)
    
    for _ in range(3):
        turnOn(pin)
        time.sleep(1)
        turnOff(pin)
        time.sleep(0.5)

    turnOn(pin)
    time.sleep(5)
    turnOff(pin)

def random_number(infested):
    """
    This function mocks the functionality of the detection.

    If tree is infested, generate number between 50-100.
    If tree is not infested, generate number between 0-50.

    Args:
        infested (bool): [description]
    """
    if infested:
        return random.randint(51, 100)
    return random.randint(0, 50)

def send_status(infested_status):
    # only update degree of infestiation and status
    doc_ref.update({
        u'infestation': random_number(infested=infested_status),
        u'status': u'measuring'
    })

def trigger_detection(BUTTON_PINS):
    """
    On button press, trigger the send process of the message.

    Args:
        PIN_NO (int): Pin number on raspi zero board
    """

    a, b = BUTTON_PINS
    infested_inp = GPIO.input(a)
    healthy_inp = GPIO.input(b)

    if infested_inp:
        print("tree infested :(")
        t1 = threading.Thread(target=send_status, args=[True])
        t2 = threading.Thread(target=blink, args=[RED])
    elif healthy_inp:
        print("tree healthy :)")
        t1 = threading.Thread(target=send_status, args=[False])
        t2 = threading.Thread(target=blink, args=[GREEN])

    if infested_inp or healthy_inp:
        t1.start()
        t2.start()

        t1.join()
    time.sleep(0.05) # debouncing


if __name__ == "__main__":
    print("+++ borki initialized +++")

    try:
        while True:
            trigger_detection((BUTTON_1, BUTTON_2))
    except KeyboardInterrupt:
        GPIO.cleanup()
    
