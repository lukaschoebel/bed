#!/usr/bin/python
import time
import random
import RPi.GPIO as GPIO
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("secrets/firestore-creds.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# reference to the firestore document
doc_ref = db.collection(u'current_measure').document(u'0')

count = 0
prev_inp = 1

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

def trigger_detection(PIN_NO):
    """
    On button press, trigger the send process of the message.

    Args:
        PIN_NO (int): Pin number on raspi zero board
    """
    global prev_inp
    global count

    t1 = time.time()
    inp = GPIO.input(PIN_NO)
    duration = time.time() - t1

    if ((not prev_inp) and inp):
        count = count + 1
        print("Button pressed")
        print(round(duration, 2))
        if duration > 0.8:
            print("befallen")
        else:
            print("cool")
        print(count)

        # only update degree of infestiation and duration
        doc_ref.update({
            u'duration': 5,
            u'infestation': random_number(infested=True),
            u'status': u'completed'
        })

    prev_inp = inp
    time.sleep(0.05)


@DeprecationWarning
if __name__ == "__main__":
    print("+++ borki initialized +++")

    try:
        while True:
            trigger_detection(18)
    except KeyboardInterrupt:
        GPIO.cleanup()
    
