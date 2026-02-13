<h1 align="center">🤚 Touchless Vision-Controlled Door Unlock System</h1>

<p align="center">
  <img src="https://img.shields.io/badge/ComputerVision-MediaPipe-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Arduino-Embedded-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Serial-Communication-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/IoT-Integration-success?style=for-the-badge"/>
</p>

---

<h2>📌 Overview</h2>

This project implements a **touchless smart unlocking mechanism** where computer vision detects a hand gesture and sends a command to an Arduino-controlled actuator.

It demonstrates real-world integration of:

* Computer Vision
* Embedded Systems
* Serial Communication
* Cyber-Physical Control

The system serves as a modular base for future smart security deployments.

---

<h2>🏗 System Flow</h2>

Camera Input
→ Python Gesture Detection
→ Serial Unlock Command
→ Arduino Processing
→ Servo Actuation

---

<h2>📁 Project Structure</h2>

```
gesture_unlock.py
arduino_unlock.ino
README.md
```

---

<h2>🧰 Requirements</h2>

<h3>Hardware</h3>

* Arduino Uno
* Servo Motor
* USB Cable
* Webcam
* Jumper Wires

<h3>Software</h3>

* Python 3.8+
* Arduino IDE

---

<h2>⚙️ Python Dependency Installation</h2>

Install required packages:

```
pip install mediapipe opencv-python pyserial
```

Verify installation:

```
python -c "import cv2, mediapipe, serial"
```

---

<h2>🔌 Finding the Correct COM Port</h2>

<h3>Windows</h3>

1️⃣ Open Device Manager
2️⃣ Expand **Ports**
3️⃣ Locate Arduino entry

Example:

```
COM3
```

Update Python file accordingly.

<h3>Linux / Raspberry Pi</h3>

```
ls /dev/tty*
```

Common outputs:

```
/dev/ttyACM0
/dev/ttyUSB0
```

---

<h2>🔧 Arduino Setup</h2>

1️⃣ Open Arduino IDE
2️⃣ Upload `arduino_unlock.ino`
3️⃣ Close Serial Monitor

<h3>Servo Wiring</h3>

| Servo Wire | Arduino |
| ---------- | ------- |
| Red        | 5V      |
| Brown      | GND     |
| Yellow     | Pin 9   |

⚠️ External power recommended for stability

---

<h2>▶️ Running the System</h2>

1️⃣ Connect Arduino
2️⃣ Upload firmware
3️⃣ Run Python script

```
python gesture_unlock.py
```

4️⃣ Hold hand steady for 2 seconds
5️⃣ Door unlock signal triggers

Press **Q** to exit

---

<h2>⚠️ Do's & Don'ts</h2>

✔ Ensure correct COM port configuration
✔ Maintain proper lighting for vision detection
✔ Close Serial Monitor before running Python
✔ Share ground if using external servo power

✘ Avoid multiple applications accessing serial port
✘ Avoid powering servo solely via weak USB
✘ Avoid obstructing camera view

---

<h2>🚀 Future Enhancements</h2>

* Gesture classification models
* Face + gesture authentication
* Wireless unlocking
* Cloud logging dashboards
* Edge deployment on Raspberry Pi

---

<p align="center">
Built for exploration in Embedded AI & Intelligent IoT Security Systems
</p>
