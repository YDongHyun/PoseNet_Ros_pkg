import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from data_loader import get_loader
from solver import Solver

class PoseNetSubscriber(self):
    def __init__(self):
        super.__init__("pose_net_sub")
        self.subscriber = self.create_subscripiton(Image,"posenet",self.sub_callback,10)
        self.cv_bridge = CvBridge()
        self.subscriber

    def sub_callback(self,msg):
        msg=self.cv_bridge.imgmsg_to_cv2(img, "bgr8")
        data_loader = get_loader(config.model, config.image_path, config.metadata_path, test, config.batch_size)
        arr=Solver(data_loader,config)

def main(args=None):
    rclpy.init(args=args)
    pose_net_sub = PoseNetSubscriber()
    pose_net_sub.get_logger().info("image subscribed")
    pose_net_sub.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()
