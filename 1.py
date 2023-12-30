import firebase_admin
from firebase_admin import credentials, db
import time
import cv2
import random
import threading

# Replace with your Firebase project credentials
cred = credentials.Certificate("/home/pi/Desktop/123/predictive-maintainence-1841d-firebase-adminsdk-oejc1-93d9f4abb4.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://predictive-maintainence-1841d-default-rtdb.firebaseio.com/'})

# Define the path in the Firebase Realtime Database
belt = '/BELT POSITION'
current = '/CURRENT'
position = '/POSITION'
rpm = '/RPM'
sound = '/SOUND DECIBEL'
temp = '/TEMPERATURE'
vis = '/OIL VISCOSITY'
volt = '/VOLTAGE'

# Set the desired display size
display_width = 640
display_height = 480

# Set webcam capture properties
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

# Function to retrieve Firebase data and process it
def firebase_thread():
    while True:
        # Retrieve Firebase data
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

        # Sleep for a short time to avoid continuous requests
        time.sleep(0.1)

# Start the Firebase thread
firebase_thread = threading.Thread(target=firebase_thread)
firebase_thread.start()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read a frame.")
        break

    # Draw rectangles and labels for each sensor
    # (rest of the code)

    # Resize the frame to the desired display size
    frame = cv2.resize(frame, (display_width, display_height))

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
