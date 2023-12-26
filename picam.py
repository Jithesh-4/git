import cv2
import random

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read a frame.")
        break

    # Generate random values for each sensor
    sensor1_value = random.randint(10, 100)
    sensor2_value = random.randint(50, 150)
    sensor3_value = random.randint(100, 200)
    sensor4_value = random.randint(200, 300)
    sensor5_value = random.randint(300, 400)

    # Draw rectangles and labels for each sensor
    cv2.rectangle(frame, (50, 50), (200, 250), (0, 255, 0), 2)
    cv2.putText(frame, f"Sensor 1: {sensor1_value}", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.rectangle(frame, (250, 50), (400, 250), (255, 0, 0), 2)
    cv2.putText(frame, f"Sensor 2: {sensor2_value}", (250, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv2.rectangle(frame, (450, 50), (600, 250), (0, 0, 255), 2)
    cv2.putText(frame, f"Sensor 3: {sensor3_value}", (450, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.rectangle(frame, (650, 50), (800, 250), (255, 255, 0), 2)
    cv2.putText(frame, f"Sensor 4: {sensor4_value}", (650, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    cv2.rectangle(frame, (850, 50), (1000, 250), (255, 0, 255), 2)
    cv2.putText(frame, f"Sensor 5: {sensor5_value}", (850, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
