# UAV Drone Detection

A ROS2-based people detection system for UAV drones using YOLOv8.

## Overview
This package uses a YOLOv8n model trained on the VisDrone dataset to detect people from a drone-mounted Raspberry Pi camera. Detections are published as ROS2 topics that can be used for obstacle avoidance or tracking.

## Stack
- ROS2 Jazzy
- YOLOv8n (Ultralytics)
- Raspberry Pi + Pi Camera
- VisDrone Dataset

## Setup

### 1. Install ROS2 Jazzy
Follow the official ROS2 Jazzy install guide for Ubuntu 24.04.

### 2. Clone the repo
```
git clone https://github.com/aleks504/UAV_drone_detection.git
cd UAV_drone_detection
```

### 3. Install dependencies
```
pip3 install ultralytics roboflow --break-system-packages
sudo apt install ros-jazzy-cv-bridge ros-jazzy-v4l2-camera
```

### 4. Build the workspace
```
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash
```

### 5. Download the dataset (for training)
Get the VisDrone dataset from Roboflow:
- Go to universe.roboflow.com
- Search "VisDrone"
- Download in YOLOv8 format

### 6. Get the trained model
Download best.pt from the team Google Drive and place it at:
```
~/drone_ws/best.pt
```

## Training
Train the model using Google Colab (recommended):
- Open training/train.py in Colab
- Set runtime to T4 GPU
- Run all cells
- Download best.pt when complete

## Running

### Launch camera node
```
ros2 run v4l2_camera v4l2_camera_node --ros-args -p image_size:="[640,480]"
```

### Launch inference node
```
ros2 run drone_perception inference_node
```

### View detections
```
ros2 topic echo /detections
```

## Topics
| Topic | Type | Description |
|-------|------|-------------|
| /camera/image_raw | sensor_msgs/Image | Raw camera frames |
| /detections | std_msgs/String | JSON detections with bbox + confidence |
