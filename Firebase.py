import firebase_admin
from firebase_admin import credentials, db
import time

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

while True:
    try:
        # Get data from Firebase
        data0 = db.reference(belt).get()
        data1= db.reference(current).get()
        data2= db.reference(position).get()
        data3= db.reference(rpm).get()
        data4= db.reference(sound).get()
        data5= db.reference(temp).get()
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

    except Exception as e:
        print("Error:", e)

    time.sleep(0.5)  # Adjust the delay based on your requirements
