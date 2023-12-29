import cv2
import numpy as np
import pyautogui
import threading

# Function to handle camera capture and eye detection
def capture_and_detect():
    global frame
    global exit_flag

    # Load the pre-trained Haar Cascade classifier for eyes
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    while not exit_flag:
        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error capturing frame.")
            break

        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # Convert the frame to grayscale for eye detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect eyes in the frame
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            # Calculate the center of the bounding box
            center_x, center_y = ex + ew // 2, ey + eh // 2

            # Move the mouse smoothly to the center of the bounding box
            pyautogui.moveTo(center_x, center_y, duration=0.2)

        # Display the frame
        cv2.imshow("Eye Detection", frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Open the camera
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error opening camera.")
    exit()

frame = None
exit_flag = False

# Start a separate thread for capturing and detecting
thread = threading.Thread(target=capture_and_detect)
thread.start()

# Wait for the user to press 'q' to exit
while cv2.waitKey(1) & 0xFF != ord('q'):
    pass

# Set the exit flag to True and wait for the thread to finish
exit_flag = True
thread.join()

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
