import sys
sys.path.append("/home/ydh/posenet_pkg/posenet_pkg/posenet_pkg")
import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Pose

class SixdofSubscriber(Node):
    def __init__(self):
        super().__init__("Sixdof_subscriber")
        self.subscriber = self.create_subscription(Pose,'sixdof',self.sub_callback,10)
        self.subscriber

    def sub_callback(self,msg):
        print("Position")
        print("x =",msg.position.x,"y =",msg.position.y,"z =",msg.position.z)
        print("Orientation")
        print("x =",msg.orientation.x,"y =",msg.orientation.y,"z =",msg.orientation.z)
        
def main(args=None):
    rclpy.init(args=args)
    node= SixdofSubscriber()
    try:
        node.get_logger().info("Waitting msg....")
        rclpy.spin(node)
        
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__=="__main__":
    main()
