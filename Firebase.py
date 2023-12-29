import firebase_admin
from firebase_admin import credentials, db
import time
import cv2
import random

# Replace with your Firebase project credentials
cred = credentials.Certificate("/home/pi/Desktop/git/fir-demo-c7e7a-firebase-adminsdk-ettih-ec76f9b27c.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://fir-demo-c7e7a-default-rtdb.firebaseio.com/'})

# Define the path in the Firebase Realtime Database
belt = '/Belt'
current = '/Current'
position = '/Position'
rpm = '/RPM'
sound = '/Sound Decibel'
temp = '/Temperature'
vis = '/Viscosity'
volt = '/Voltage'

display_width = 800  # Set the desired width
display_height = 600  # Set the desired height

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read a frame.")
        break

    # Get data from Firebase
    data0 = db.reference(belt).get()
    data1 = db.reference(current).get()
    data2 = db.reference(position).get()
    data3 = db.reference(rpm).get()
    data4 = db.reference(sound).get()
    data5 = db.reference(temp).get()
    data6 = db.reference(vis).get()
    data7 = db.reference(volt).get()

    if data0 is not None:
        # Process the received data
        print("Belt:", data0)
        print("Current:", data1)
        print("Position:", data2)
        print("RPM:", data3)
        print("Sound Decibel:", data4)
        print("Temperature:", data5)
        print("Viscosity:", data6)
        print("Voltage:", data7)

        # Add your logic here to perform actions based on the received data
        # For example, you can control GPIO pins, sensors, actuators, etc.

    # Generate random values for each sensor
    sensor1_value = data0
    sensor2_value = data1
    sensor3_value = data2
    sensor4_value = data3
    sensor5_value = data4
    sensor6_value = data5
    sensor7_value = data6
    sensor8_value = data7

    # Draw rectangles and labels for each sensor
    cv2.rectangle(frame, (50, 50), (200, 250), (0, 255, 0), 2)
    cv2.putText(frame, f"Belt: {sensor1_value}", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.rectangle(frame, (250, 50), (400, 250), (255, 0, 0), 2)
    cv2.putText(frame, f"Current: {sensor2_value}", (250, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv2.rectangle(frame, (450, 50), (600, 250), (0, 0, 255), 2)
    cv2.putText(frame, f"Position: {sensor3_value}", (450, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.rectangle(frame, (650, 50), (800, 250), (255, 255, 0), 2)
    cv2.putText(frame, f"RPM: {sensor4_value}", (650, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    cv2.rectangle(frame, (850, 50), (1000, 250), (255, 0, 255), 2)
    cv2.putText(frame, f"Sound Decibel: {sensor5_value}", (850, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
    
    cv2.rectangle(frame, (850, 50), (1000, 250), (255, 0, 255), 2)
    cv2.putText(frame, f"Temperature: {sensor6_value}", (850, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
    
    cv2.rectangle(frame, (850, 50), (1000, 250), (255, 0, 255), 2)
    cv2.putText(frame, f"Viscosity: {sensor7_value}", (850, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
    
    cv2.rectangle(frame, (850, 50), (1000, 250), (255, 0, 255), 2)
    cv2.putText(frame, f"Voltage: {sensor8_value}", (850, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
    
    # Resize the frame to the desired display size
    frame = cv2.resize(frame, (display_width, display_height))

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
