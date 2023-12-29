import cv2
import numpy as np
import pytesseract

def perform_ocr(image):
    try:
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(image)

        # Print the extracted text
        print("Extracted Text:\n", text)

    except Exception as e:
        print("An error occurred:", str(e))

def main():
    # Load the pre-trained YOLO model for object detection
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layer_names = net.getUnconnectedOutLayersNames()

    # Open the camera (use 0 for the default camera)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Object detection using YOLO
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(layer_names)

        # Extract information about detected objects
        confidences = []
        class_ids = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * frame.shape[1])
                    center_y = int(detection[1] * frame.shape[0])
                    w = int(detection[2] * frame.shape[1])
                    h = int(detection[3] * frame.shape[0])

                    # Extract the region of interest (ROI) containing the detected object
                    roi = frame[center_y - h // 2:center_y + h // 2, center_x - w // 2:center_x + w // 2]

                    # Perform OCR on the ROI
                    perform_ocr(roi)

        # Display the frame
        cv2.imshow("Object Detection and OCR", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
