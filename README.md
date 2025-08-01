# 🎯 YOLOv8 Object Detection with ESP32-CAM Streaming

A real-time object detection system that integrates an **ESP32-CAM** and **YOLOv8** to identify objects from a live camera feed over WiFi. Detects people, animals, vehicles, and more using a pre-trained **COCO** model.

---

## 📸 Project Highlights

- 🧠 **YOLOv8 Detection**: Fast and accurate object detection using the latest YOLOv8 model.
- 📷 **ESP32-CAM Integration**: Stream camera images over WiFi directly to your Python application.
- 🎛️ **Multiple Resolutions**: Choose between high, medium, and low quality streaming.
- 🧰 **Lightweight Setup**: Python script + low-cost ESP32-CAM module = portable detection system.

---

## 🛠️ Requirements

### Python (PC-Side)
- Python 3.x
- Required packages:
  ```bash
  pip install opencv-python numpy ultralytics
  ```

### ESP32-CAM
- ESP32-CAM module
- Arduino IDE with ESP32 support
- Required Arduino libraries:
  - `esp32cam`
  - `WebServer`

---

## ⚙️ Setup Guide

### 🔧 ESP32-CAM

1. **Open Arduino IDE** and install libraries:
   - Go to **Sketch > Include Library > Manage Libraries**
   - Search for and install `esp32cam`, `WebServer`

2. **Configure and Upload Code**:
   - Add your WiFi credentials in the ESP32 code:
     ```cpp
     const char* ssid = "YOUR_SSID";
     const char* password = "YOUR_PASSWORD";
     ```
   - Upload code to ESP32-CAM via FTDI programmer.

3. **Get IP Address**:
   - Open **Serial Monitor** after upload to view assigned IP address.
   - Example: `http://192.168.1.100/cam-hi.jpg`

---

### 🐍 Python Script

1. **Set the ESP32-CAM URL** in your script:
   ```python
   url = "http://<ESP32-IP>/cam-hi.jpg"
   ```

2. **Run the Python script**:
   ```bash
   python script.py
   ```

3. **View Results**:
   - A window will display images with real-time object detection.
   - Press `q` to exit.

---

## 🔍 Object Detection Details

- **Model**: YOLOv8 pre-trained on the [COCO dataset](https://cocodataset.org/#home)
- **Classes**: 80 object types including:
  - People: 🧍‍♂️🧍‍♀️
  - Animals: 🐶 🐱 🐦
  - Vehicles: 🚗 🚌 🏍️
  - Daily Items: 🪑 📦 🍎 📚

---

## 🧾 Code Overview

### Python Script
- `ultralytics.YOLO` loads the model
- `cv2.VideoCapture` or `requests.get()` fetches image from ESP32
- Object detection runs per frame
- Results shown using OpenCV

### ESP32-CAM Arduino Code
- Sets up camera with multiple JPEG endpoints:
  - `/cam-lo.jpg`, `/cam-hi.jpg`, etc.
- Starts web server for image access

---

## 📂 Project Structure

```
YOLO-ESP32-Detection/
├── script.py             # Python script for detection
├── esp32cam_code.ino     # Arduino sketch
├── README.md             # Project documentation
├── static/               # Optional saved images
└── requirements.txt      # Python dependencies
```

---

## 📜 License

This project is licensed under the **MIT License**.  
Use freely for learning, experimentation, or improvement!

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to:
- Submit pull requests
- Report bugs
- Suggest new features

---

## 📷 Preview

![Preview](static.png)

---

> Created with ❤️ using OpenCV, Ultralytics, and the awesome ESP32-CAM board.
