import rclpy
import cv2
from rclpy.node import Node
from rclpy.qos import QoSProfile
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge

class Image_pub(Node):
    def __init__(self):
        super().__init__('image_pub')
        qos_profile = QoSProfile(depth=10)
        self.image_pub=self.create_publisher(CompressedImage,'/CompressedImage',qos_profile)
        self.cv_bridge = CvBridge()
        #self.timer=self.create_timer(1,self.publish_image_msg)

    def publish_image_msg(self): 
        msg=CompressedImage()
        vid_data = cv2.VideoCapture('/dev/video0',cv2.CAP_V4L)
        vid_data.set(3,640)
        vid_data.set(4,480)
        #while(vid_data.isOpened()):
        ret,image=vid_data.read()            
        msg=self.cv_bridge.cv2_to_compressed_imgmsg(image)
        self.image_pub.publish(msg)
        print("published")
        vid_data.release()

def main(args=None):
    rclpy.init(args=args)
    node=Image_pub()
    try:
        while(1):
            rclpy.spin_once(node)
            node.publish_image_msg()

    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')

    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    main()
