#!/usr/bin/python
import time
import random
import RPi.GPIO as GPIO
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("secrets/firestore-creds.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# reference to the firestore document
doc_ref = db.collection(u'current_measure').document(u'0')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # button 1
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # button 2
GPIO.setup(12, GPIO.OUT)     # set output for red
GPIO.setup(19, GPIO.OUT)    # set output for green
GPIO.setup(6, GPIO.OUT)    # set output for blue

# red = GPIO.PWM(19, 75)      # create object red for PWM on port 17  
# green = GPIO.PWM(16, 75)    # create object green for PWM on port 27   
# blue = GPIO.PWM(6, 75)     # create object blue for PWM on port 22 
LED_PIN = 19
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
    global LED_PIN

    a, b = PINS
    infested_inp = GPIO.input(a)
    healthy_inp = GPIO.input(b)

    if infested_inp:
        print("tree infested :(")
        infested_status = True
        LED_PIN = 19
    elif healthy_inp:
        print("tree healthy :)")
        infested_status = False
        LED_PIN = 6
    

    if infested_inp or healthy_inp:
        GPIO.output(LED_PIN, GPIO.HIGH)
        # only update degree of infestiation and duration
        doc_ref.update({
            u'infestation': random_number(infested=infested_status),
            u'status': u'measuring'
        })

    time.sleep(0.05)
    GPIO.output(LED_PIN, GPIO.LOW)


if __name__ == "__main__":
    print("+++ borki initialized +++")

    try:
        while True:
            trigger_detection((17, 18))
    except KeyboardInterrupt:
        GPIO.cleanup()
    
