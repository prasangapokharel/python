import cv2
import numpy as np

# Define target colors
targets = {
    "Yellow": ([20, 100, 100], [30, 255, 255]),  # Yellow color range in HSV
    "Red": ([(0, 100, 100), (10, 255, 255)], [(160, 100, 100), (180, 255, 255)]),  # Red color range in HSV
    "Blue": ([100, 100, 100], [130, 255, 255])  # Blue color range in HSV
}

# Color names and corresponding BGR colors for labeling
color_labels = {
    "Yellow": (0, 255, 255),
    "Red": (0, 0, 255),
    "Blue": (255, 0, 0)
}

# Function to detect and label colors
def detect_colors(frame):
    # Convert the frame to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Detect and label colors
    for color_name, (lower, upper) in targets.items():
        if isinstance(lower[0], tuple):  # Check if it's a range with two tuples
            for (lower_range, upper_range) in zip(lower, upper):
                # Create a mask for the current color range
                mask = cv2.inRange(hsv_frame, np.array(lower_range), np.array(upper_range))
                process_mask(mask, frame, color_name)
        else:
            mask = cv2.inRange(hsv_frame, np.array(lower), np.array(upper))
            process_mask(mask, frame, color_name)

    return frame

# Function to process the mask and add labels
def process_mask(mask, frame, color_name):
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Find the largest contour
        max_contour = max(contours, key=cv2.contourArea)

        # Get the bounding box of the largest contour
        x, y, w, h = cv2.boundingRect(max_contour)

        # Draw a rectangle and put text on the frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), color_labels[color_name], 2)
        cv2.putText(frame, color_name, (x - 20, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color_labels[color_name], 2)

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect and label colors in the frame
    result_frame = detect_colors(frame)

    # Display the result
    cv2.imshow("Color Detection", result_frame)

    # Exit the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
