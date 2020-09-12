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
    
    # reference to the firestore document
    doc_ref = db.collection(u'current_measure').document(u'0')

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


def myInterrupt(channel):
    # reference to the firestore document
    doc_ref = db.collection(u'current_measure').document(u'0')
    
    start_time = time.time()

    # Wait for the button up
    while GPIO.input(channel) == 0:
        pass

    time.sleep(0.05)
    buttonTime = time.time() - start_time    # How long was the button down?


    print(buttonTime)
    if .1 <= buttonTime < 2:    # Ignore noise
        buttonStatus = 1        # 1= brief push
        print("healthy af :)")
        infested = False
    else:
        buttonStatus = 2        # 2= Long push
        print("not healthy :(")
        infested = True

    doc_ref.update({
        u'duration': 5,
        u'infestation': random_number(infested=infested),
        u'status': u'completed'
    })


if __name__ == "__main__":
    # try:
    #     while True:
    #         trigger_detection(PIN_NO=18)
    # except KeyboardInterrupt:
    #     GPIO.cleanup()
    print("hi")
    GPIO.add_event_detect(18, GPIO.FALLING, callback=myInterrupt, bouncetime=500)
    msg = input("press enter to exit\n")
    GPIO.cleanup()