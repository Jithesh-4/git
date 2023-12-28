import RPi.GPIO as GPIO
import time
import random
from firebase_admin import credentials, initialize_app, db

# Replace the following with your Firebase project credentials
cred = credentials.Certificate("/home/pi/Desktop/git/predictive-maintainence-1841d-firebase-adminsdk-oejc1-93d9f4abb4.json")
firebase_app = initialize_app(cred, {"databaseURL": "https://predictive-maintainence-1841d-default-rtdb.firebaseio.com/"})

# Replace this with the path where you want to store sensor data in Firebase
sensor_data_ref = db.reference("/")

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin to which the RPM sensor is connected
rpm_sensor_pin = 17

# Set up the GPIO pin as input
GPIO.setup(rpm_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize variables
rpm_count = 0
prev_time = time.time()

# Define a callback function for the RPM sensor interrupt
def rpm_callback(channel):
    global rpm_count
    rpm_count += 1

# Add event detection to the RPM sensor GPIO pin
GPIO.add_event_detect(rpm_sensor_pin, GPIO.FALLING, callback=rpm_callback)


try:
    while True:
            # Calculate RPM every 5 seconds
        current_time = time.time()
        elapsed_time = current_time-prev_time
        prev_time = current_time

            # Calculate RPM
        rpm = (rpm_count / 2) / elapsed_time * 60
        print(f"RPM: {rpm}")

            # Reset RPM count
        rpm_count = 0
            
        sensor_data_ref.child("RPM").set(rpm)
        time.sleep(1)  # Upload data every 60 seconds (adjust as needed)
except KeyboardInterrupt:
    print("Program terminated by user.")
    
finally:
    firebase_app.delete()  # Clean up Firebase resources
    GPIO.cleanup()

if __name__ == "__main__":
    main()




    
    
