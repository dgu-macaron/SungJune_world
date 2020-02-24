#!/usr/bin/env python

import rclpy
from std_msgs.msg import String
import sys, select, tty, termios

settings = termios.tcgetattr(sys.stdin)

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def main(args=None):
    rclpy.init(args=args)
    
    node = rclpy.create_node('Key_publisher')
    pub = node.create_publisher(String, 'keyboard', 10)
    i = 0

    while True:
        key = getKey()
        if key != '\x03' and key != 0:  # '\x03' is ctrl + c
            # print(key)
            key_str = "Pub key : %s" % key  # , rospy.get_time()
            node.get_logger().info(key_str)
            msg = String()
            msg.data = key
            pub.publish(msg)
        else:
            print('stop key publisher')
            break

        i += 1
        # node.get_logger().info('%d Publishing: emergency:%d  speed:%d steer:%d' %(i, control_msg.emergency, control_msg.speed, control_msg.steer))
    rclpy.shutdown()


if __name__=='__main__':
    main()

