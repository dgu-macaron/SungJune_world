import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from my_msgs.msg import Float164
from my_msgs.msg import Int164
from my_msgs.msg import String4
from my_msgs.msg import Carcontrol1

get_key = String4()
control_msg = Carcontrol1()

def key_sub_callback(key):
        get_key = key
        
        if get_key.one == 's':
            control_msg.emergency = True
        elif get_key.one == 'w':
            control_msg.emergency = False


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('PubAndSub')
    Control_Subscriber = node.create_subscription(String4, 'key', key_sub_callback, 10)
    assert Control_Subscriber
    Control_Publisher = node.create_publisher(Carcontrol1, 'control', 10)
    i = 0
    while True:
        rclpy.spin_once(node)
        Control_Publisher.publish(control_msg)
        i += 1
        node.get_logger().info('%d Publishing: emergency:%d  speed:%d steer:%d' %(i, control_msg.emergency, control_msg.speed, control_msg.steer))
    rclpy.shutdown()


if __name__ == '__main__':
    main()
