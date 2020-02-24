import rclpy

from std_msgs.msg import String

from my_msgs.msg import Float164
from my_msgs.msg import Int164
from my_msgs.msg import String4
# from my_msgs.msg import Carcontrol1


msg = String4()

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('key_pub')
    Key_Publisher = node.create_publisher(String4, 'key', 10)
    
    i = 0
    while True:
        i += 1
        msg.one = input('문자를 입력하세요 :')
        Key_Publisher.publish(msg)
        node.get_logger().info('%d Publishing: "%s"' %(i, msg.one))


    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
