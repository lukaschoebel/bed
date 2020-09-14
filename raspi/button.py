#!/usr/bin/python3
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
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
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

def trigger_detection(PINS):
    """
    On button press, trigger the send process of the message.

    Args:
        PIN_NO (int): Pin number on raspi zero board
    """
    
    infested, healthy = PINS

    infested_inp = GPIO.input(infested)
    healthy_inp = GPIO.input(healthy)

    print(f"infested: {infested_inp}")
    print(f"healthy: {healthy_inp}")

    # only update degree of infestiation and duration
    doc_ref.update({
        u'duration': 5,
        u'infestation': random_number(infested=True),
        u'status': u'completed'
    })

    prev_inp = inp
    time.sleep(0.05)


if __name__ == "__main__":
    print("+++ borki initialized +++")

    try:
        while True:
            trigger_detection((17, 18))
    except KeyboardInterrupt:
        GPIO.cleanup()
    
