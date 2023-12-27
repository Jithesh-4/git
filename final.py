# python3 /home/pi/Desktop/car-iot.py
import time
import pyrebase
import cv2
import dlib
import imutils
import random
from imutils import face_utils
from scipy.spatial import distance as dist
import RPi.GPIO as GPIO
from threading import Thread

# INPUT PINS INITIALIZATION
GPIO.setmode(GPIO.BCM)
rpm_pin = 22
sou_pin1 = 2
sou_pin2 = 3
sou_pin3 = 4
belt_pin = 17
pos_pin = 27

GPIO.setup(rpm_pin, GPIO.IN)
GPIO.setup(sou_pin1, GPIO.IN)
GPIO.setup(sou_pin2, GPIO.IN)
GPIO.setup(sou_pin3, GPIO.IN)
GPIO.setup(belt_pin, GPIO.IN)
GPIO.setup(pos_pin, GPIO.IN)





config = {
  "apiKey": "AIzaSyCXw8rIHYKQvDsXaK8CCm2-7L5PamYbBXQ",
  "authDomain": "iot-car-dashboard-b5e3a.firebaseapp.com",
  "databaseURL": "https://iot-car-dashboard-b5e3a-default-rtdb.firebaseio.com/",
  "storageBucket": "iot-car-dashboard-b5e3a.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

print("Send Data to Firebase Using Raspberry Pi")
print("----------------------------------------")
print()

belt = False
pos = 0
acc = "low"
def parametersCalculation():
    while True:
    # acc calc
        if((GPIO.input(sou_pin1) == 1) and (GPIO.input(sou_pin2) == 0) and (GPIO.input(sou_pin3) == 0)):
            acc = "low"
        elif((GPIO.input(sou_pin1) == 1) and (GPIO.input(sou_pin2) == 1) and (GPIO.input(sou_pin3) == 0)):
            acc = "med"
        elif((GPIO.input(sou_pin1) == 1) and (GPIO.input(sou_pin2) == 1) and (GPIO.input(sou_pin3) == 1)):
            acc = "high"
        elif((GPIO.input(sou_pin1) == 0) and (GPIO.input(sou_pin2) == 0) and (GPIO.input(sou_pin3) == 0)):
            acc = "idle"
        #print(acc)


        # belt calc
        if(GPIO.input(belt_pin) == 0):
            belt = True
        elif(GPIO.input(belt_pin) == 1):
            seatbelt = False

        # pos calc
        if(GPIO.input(pos_pin) == 0):
            pos = True
        elif(GPIO.input(pos_pin) == 1):
            pos = False


        data = {
            "belt":belt,
            "pos" : pos,
            "sou" : sound,}

        print(data)

        db.child("sensor-values").set(data)
        time.sleep(2)

if name == 'main':
    Thread(target = parametersCalculation).start()
