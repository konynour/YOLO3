import cv2
import numpy as np
import urllib.request
from ultralytics import YOLO
from urllib.error import URLError, HTTPError

# Load the YOLOv8 model (e.g., yolov8n.pt)
model = YOLO("yolov8n.pt")

# URL of the ESP32-CAM video stream (replace with the actual stream URL)
# url = 'http://192.168.168.154/cam-hi.jpg'  # Make sure this is correct

# Set detection thresholds
confThreshold = 0.5  # Confidence threshold for object detection
nmsThreshold = 0.3   # Non-maximum suppression threshold for removing overlapping boxes

# Class labels (from coco.names)
classesfile = 'coco.names'  # Path to coco.names
classNames = []

with open(classesfile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Define a function to perform object detection using YOLOv8
def detect_objects(frame):
    # Perform inference with YOLOv8 model
    results = model(frame)  # This returns a list of results

    # Process the results (the first element contains the detections)
    result = results[0]

    # Access the detection boxes, confidences, and class IDs
    boxes = result.boxes  # Get the boxes
    if len(boxes) == 0:
        print("No objects detected.")
        return frame

    # Extract details from the boxes
    for box in boxes:
        # Each box contains [x1, y1, x2, y2, confidence, class_id]
        x1, y1, x2, y2 = map(int, box.xywh[0])  # Get box coordinates (center_x, center_y, width, height)
        confidence = box.conf[0]  # Confidence score for the detection
        class_id = int(box.cls[0])  # Class ID
        class_name = classNames[class_id]  # Class name from coco.names

        # Only draw the bounding box if the confidence is above the threshold
        if confidence > confThreshold:
            # Draw bounding box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
            cv2.putText(frame, f'{class_name} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

            print(f"Detected {class_name} with {confidence:.2f} confidence")

    return frame

# Main loop to read the video stream and perform object detection
while True:
    try:
        # Read the image from the ESP32-CAM stream
        img_resp = urllib.request.urlopen(url)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        im = cv2.imdecode(imgnp, -1)

        # Perform object detection on the frame
        im = detect_objects(im)

        # Display the resulting image with detections
        cv2.imshow('Object Detection', im)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except (URLError, HTTPError) as e:
        print(f"Error fetching image from ESP32-CAM: {e}")
        break

# Clean up
cv2.destroyAllWindows()