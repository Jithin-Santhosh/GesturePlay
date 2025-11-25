# GesturePlay
GesturePlay is a Python-based tool that uses your webcam and modern computer vision to control browser-based games solely through hand movements. Leveraging MediaPipe and OpenCV, the app recognizes specific hand gestures and maps them to keyboard actions—no physical keyboard or gamepad needed!

Features
Real-time webcam hand gesture recognition

Maps gestures to keyboard (WASD/arrows) for game control

Works with any browser game using keyboard input

Demo included for the racing game TOP SPEED 3D

Flexible logic—easily modify for different games or controls

How it Works
Starts your webcam and detects hand or finger position using MediaPipe.

Maps your hand movements to keyboard events (e.g., move hand left/right to steer).

Sends those events to the browser game window, allowing hands-free gameplay.

Requirements
Python 3.10 or 3.11

OpenCV, MediaPipe, pynput packages

Setup & Usage
bash
# Create and activate your virtual environment
python -m venv webcam-game-env
webcam-game-env\Scripts\activate

# Install dependencies
python -m pip install opencv-python mediapipe pynput

# Run the controller
python index.py
Start your browser game (e.g., TOP SPEED 3D), and control it with your hand gestures using your webcam.

Demo
See demo.gif or watch the video included in the repo for gameplay using WebcamGameController in TOP SPEED 3D!
