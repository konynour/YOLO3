# YOLOv8 Object Detection with ESP32-CAM Streaming

## Overview
This project demonstrates real-time object detection using the **YOLOv8** model with images streamed from an ESP32-CAM. The Python script captures images from the ESP32-CAM, detects objects (e.g., cats, birds, people, and cars), and displays the annotated results. The model is trained using the **COCO dataset**, which includes 80 different classes of common objects.

## Features
- **Real-Time Object Detection**: Utilizes YOLOv8 to detect and annotate objects in real-time.
- **ESP32-CAM Integration**: Streams images from an ESP32-CAM over WiFi.
- **Resolution Options**: Supports various image resolutions (low, medium, high) from the ESP32-CAM.
- **Pre-Trained Model**: Utilizes a YOLOv8 model pre-trained on the **COCO dataset**, capable of detecting objects like cats, dogs, people, vehicles, and more.

## Requirements

### Python Script
- **Python 3.x**
- Required libraries:
  - `opencv-python` (for image processing)
  - `numpy` (for handling arrays)
  - `ultralytics` (for YOLOv8 object detection)

To install the required libraries, you can run the following command:
```bash
pip install opencv-python numpy ultralytics














YOLOv8 Object Detection with ESP32-CAM Streaming
Overview
This project demonstrates real-time object detection using the YOLOv8 model with images streamed from an ESP32-CAM. The Python script captures images from an ESP32-CAM, detects objects, and displays annotated results, including categories like people, animals, and vehicles.

Features
Real-Time Object Detection: Uses YOLOv8 to detect and annotate objects.
ESP32-CAM Integration: Streams images from the ESP32-CAM over WiFi.
Resolution Options: Supports multiple image resolutions (low, medium, high) for streaming.
Requirements
Python Script
Python 3.x
Required libraries: opencv-python, numpy, ultralytics
Install the necessary libraries with:

bash
Copy code
pip install opencv-python numpy ultralytics
ESP32-CAM Setup
ESP32-CAM module
Arduino IDE with ESP32 support
WiFi network credentials
Ensure that you have the esp32cam and WebServer libraries installed in your Arduino IDE:

Go to Sketch > Include Library > Manage Libraries.
Search for and install the required libraries.
Setup
ESP32-CAM Code
Install the Required Libraries
Ensure that the esp32cam and WebServer libraries are installed in your Arduino IDE.

Upload the Code
Open the Arduino IDE.
Paste the ESP32-CAM code into a new sketch.
Upload the code to your ESP32-CAM.
Connect to WiFi
Replace the WIFI_SSID and WIFI_PASS in the ESP32-CAM code with your WiFi credentials.

Obtain the IP Address
After uploading the code, open the Serial Monitor in the Arduino IDE to view the ESP32-CAM’s IP address. You will use this IP to access the camera stream.

Python Script
Configure the URL
In the Python script, replace the url variable with the IP address of your ESP32-CAM, followed by the image path (e.g., http://<ESP32-IP>/cam-hi.jpg).

Run the Script
To start capturing and processing images from the ESP32-CAM, navigate to the directory containing the script and run:

bash
Copy code
python script.py
View the Output
The script will open a window displaying the image with detected objects. Press the 'q' key to close the window and stop the stream.

Object Detection Classes
The YOLOv8 model is pre-trained on the COCO Dataset, which includes 80 object classes. Examples of detectable objects include:

People: Humans in various poses and situations.
Animals: Cats, dogs, birds, etc.
Vehicles: Cars, buses, trucks, bicycles, and motorcycles.
Everyday Objects: Chairs, cups, books, bottles, and more.
For a full list of object classes, refer to the official COCO dataset documentation.

Code Overview
Python Script
Model Initialization: Loads the YOLOv8 model for object detection using the ultralytics library.
Image Handling: Fetches images from the ESP32-CAM URL using OpenCV.
Object Detection: Processes images using YOLOv8 to detect and annotate objects.
Display: Displays the annotated images in a window that can be closed by pressing the 'q' key.
ESP32-CAM Code
Camera Setup: Initializes the ESP32-CAM with different resolutions (low, medium, high).
Web Server: Configures a web server to stream JPEG images at various resolutions.
Endpoint Handlers: Handles requests for different resolutions (e.g., cam-hi.jpg for high resolution, cam-lo.jpg for low resolution).
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Feel free to contribute to this project by opening issues or submitting pull requests for improvements or additional features.

This README includes all the required sections, along with detailed steps for both the ESP32-CAM and Python script setups. Let me know if you'd like any further adjustments or additions!






