import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
from ultralytics import YOLO
import json

class InferenceNode(Node):
    def __init__(self):
        super().__init__('inference_node')
        self.bridge = CvBridge()

        # Load your trained model
        self.model = YOLO('/home/uav/drone_ws/best.pt')

        # Subscribe to Pi camera topic
        self.sub = self.create_subscription(
            Image,
            '/image_raw',
            self.image_callback,
            10)

        # Publish detections as JSON
        self.pub = self.create_publisher(String, '/detections', 10)
        self.get_logger().info('Inference node ready!')

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        results = self.model(frame, conf=0.01,verbose=True)[0]

        detections = []
        for box in results.boxes:
            detections.append({
                'class': self.model.names[int(box.cls)],
                'confidence': round(float(box.conf), 2),
                'bbox': box.xywhn.tolist()[0]
            })

        out = String()
        out.data = json.dumps(detections)
        self.pub.publish(out)

        if detections:
            self.get_logger().info(f'Detected {len(detections)} person(s)')

def main(args=None):
    rclpy.init(args=args)
    node = InferenceNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
