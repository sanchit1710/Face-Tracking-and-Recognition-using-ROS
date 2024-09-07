# Face Tracking and Recognition using ROS, Arduino, Servo Motor, and Camera
# Project Overview
This project implements a face tracking and detection system using a camera, a servo motor, ROS (Robot Operating System), and an Arduino. The system detects a face in real-time and adjusts the camera's orientation using the servo motor to keep the face centered in the frame.

# Key Features
1) Face Detection: The system uses OpenCV for face detection.
2) Servo Motor Control: The servo motor is controlled by Arduino and adjusts the camera position to track the face.
3) ROS Integration: ROS is used to handle the communication between the camera, the face detection algorithm, and the Arduino.
4) Real-time Tracking: The camera moves in real-time, following the detected face as it moves.

# Components Used
Camera: For capturing live video feed.
Servo Motor: To adjust the camera's position (pan and tilt).
Arduino: For controlling the servo motor.
ROS (Robot Operating System): For communication between the components.
OpenCV: For face detection.

# Prerequisites
Before running the project, make sure you have the following dependencies installed:
1. ROS (Noetic recommended)
2. OpenCV
3. Arduino IDE
4. Python 3 (for ROS nodes)
5. Arduino-ROS bridge package

# Hardware Setup
Servo Motor: Connect the servo motor to the Arduino's PWM pin (e.g., pin 9).
Camera: Mount the camera in a way that it can rotate horizontally using the servo motor.
Arduino: Upload the provided Arduino code to control the servo based on the commands received from ROS.

# Usage
1. Connect the camera and Arduino to your computer.
2. Run the ROS nodes in the respective terminals.
3. The system will start detecting a face in the camera feed, and the servo motor will rotate the camera to track the face.

# Future Improvements
1. Add a second servo for vertical (tilt) control.
2. Optimize the face detection algorithm for faster tracking.
3. Integrate more advanced face recognition to track specific individuals.

# Troubleshooting
1. If the servo motor is not responding, check the serial communication between ROS and Arduino.
2. Ensure that the camera feed is correctly published to the ROS topic.
