import RPi.GPIO as GPIO
import time
import firebase_admin
from firebase_admin import credentials, firestore

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin to which the RPM sensor is connected
rpm_sensor_pin = 17

# Set up the GPIO pin as input
GPIO.setup(rpm_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize variables
rpm_count = 0
prev_time = time.time()

# Initialize Firebase
cred = credentials.Certificate("/home/pi/Desktop/git/fir-demo-c7e7a-firebase-adminsdk-ettih-ec76f9b27c.json")
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore database
db = firestore.client()

# Define a callback function for the RPM sensor interrupt
def rpm_callback(channel):
    global rpm_count
    rpm_count += 1

# Add event detection to the RPM sensor GPIO pin
GPIO.add_event_detect(rpm_sensor_pin, GPIO.FALLING, callback=rpm_callback)

try:
    while True:
        # Calculate RPM every 1 seconds
        time.sleep(1)
        current_time = time.time()
        elapsed_time = current_time - prev_time
        prev_time = current_time

        # Calculate RPM
        rpm = (rpm_count / 2) / elapsed_time * 60
        print(f"RPM: {rpm}")

        # Upload RPM value to Firebase Firestore
        rpm_data = {"rpm": rpm}
        db.collection("rpm_data").add(rpm_data)
        print("RPM data uploaded to Firebase")

        # Reset RPM count
        rpm_count = 0

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO on program exit
    GPIO.cleanup()
