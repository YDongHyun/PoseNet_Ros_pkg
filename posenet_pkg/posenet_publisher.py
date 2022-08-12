import rclpy
import cv2
import matplotlib.pyplot as plt
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

img_data = plt.imread('posenet_pkg/posenet_pkg/test/test.png')

class PoseNetPublisher(Node):
    def __init__(self):
        super().__init__("pose_net_pub")
        self.publisher = self.create_publisher(Image,"posenet",10)   
        self.cv_bridge = CvBridge()

    def publish_callback(self):
        img=Image()
        img=self.cv_bridge.cv2_to_imgmsg(img_data, "bgr8")
        self.publisher.publish(img)

def main(args=None):
    rclpy.init(args=args)
    pose_net_pub = PoseNetPublisher()
    pose_net_pub.get_logger().info("image published")
    pose_net_pub.destroy_node()

    rclpy.shutdown()

if __name__=="__main__":
    main()
