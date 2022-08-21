import sys
sys.path.append("/home/ydh/posenet_pkg/posenet_pkg/posenet_pkg")
import rclpy
from rclpy.node import Node 
from sensor_msgs.msg import Image as Msg_img
from geometry_msgs.msg import Pose
from PIL import Image 
import cv2
from cv_bridge import CvBridge
import torch
from data_loader import get_loader
from solver import Solver
from torch.backends import cudnn 

class PoseNetSub_Pub(Node):
    def __init__(self):
        super().__init__("posenet_sub_pub")
        self.subscriber = self.create_subscription(Msg_img,'posenet',self.sub_callback,10)
        self.publisher = self.create_publisher(Pose,'sixdof',10)   
        self.cv_bridge = CvBridge()
        self.subscriber

    def sub_callback(self,img):
        global pos
        global ori
        global flag
        flag=True
        msg=self.cv_bridge.imgmsg_to_cv2(img)
        color_coverted = cv2.cvtColor(msg, cv2.COLOR_BGR2RGB)
        pil_image=Image.fromarray(color_coverted)
        cudnn.benchmark = True
        data_loader = get_loader(model='Resnet', image_path=pil_image ,mode='test', batch_size=1)
        sol=Solver(data_loader)
        pos,ori=sol.test()
        self.get_logger().info("image subscribed")
        print("pos",pos)
        print("ori",ori)  

    def publish_callback(self):
        global flag
        msg=Pose()
        msg.position.x=float(pos[0])
        msg.position.y=float(pos[1])
        msg.position.z=float(pos[2])
        msg.orientation.x=float(ori[0])
        msg.orientation.y=float(ori[1])
        msg.orientation.z=float(ori[2])
        msg.orientation.w=0.0
        self.publisher.publish(msg)
        self.get_logger().info("6 Dof published")
        flag=False

def main(args=None):
    rclpy.init(args=args)
    node= PoseNetSub_Pub()
    try:
        node.get_logger().info("Waitting msg....")
        while(True):
            rclpy.spin_once(node)   
            if flag==True:
                node.publish_callback()
    
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__=="__main__":
    main()
