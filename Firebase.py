import firebase_admin
from firebase_admin import credentials, db
import time

# Replace with your Firebase project credentials
cred = credentials.Certificate("/home/pi/Desktop/git")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://predictive-maintainence-1841d-default-rtdb.firebaseio.com/'})

# Define the path in the Firebase Realtime Database
firebase_path = '/control_data'

while True:
    try:
        # Get data from Firebase
        data = db.reference(firebase_path).get()
        
        if data is not None:
            # Process the received data
            print("Received Data:", data)

            # Add your logic here to perform actions based on the received data

            # For example, you can control GPIO pins, sensors, actuators, etc.

    except Exception as e:
        print("Error:", e)

    time.sleep(1)  # Adjust the delay based on your requirements
