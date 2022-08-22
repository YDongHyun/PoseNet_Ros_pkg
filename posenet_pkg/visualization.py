import sys
sys.path.append("/home/ydh/posenet_pkg/posenet_pkg/posenet_pkg")
import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Pose
from PIL import Image
from PIL import ImageDraw
import numpy as np
import matplotlib.pyplot as plt

class Visualization(Node):
    def __init__(self):
        super().__init__("visualization")
        self.subscriber = self.create_subscription(Pose,'sixdof',self.sub_callback,10)
        self.subscriber

    def sub_callback(self,msg):
        image = Image.open('/home/ydh/posenet_pkg/posenet_pkg/posenet_pkg/map.png')
        image = image.resize((1400, 400))
        arr.append([(msg.position.x+50)*10,(msg.position.y+50)*10])
        for i,j in arr:
            image = pil_draw_point(image, (i,j))
        plt.imshow(np.array(image))
        plt.show()

arr=[]
 
def pil_draw_point(image, point):
    x, y = point
    draw = ImageDraw.Draw(image)
    radius = 5
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(0, 0, 255))
    return image

def main(args=None):
    rclpy.init(args=args)
    node= Visualization()
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
