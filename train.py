from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="/home/parallels/drone_ws/VisDrone-9/data.yaml",
    epochs=50,
    imgsz=416,
    batch=8,
    device="cpu",
    name="people_drone",
    degrees=20.0,
    fliplr=0.5,
    mosaic=1.0,
)
