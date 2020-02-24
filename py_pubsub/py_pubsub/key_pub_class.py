import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from my_msgs.msg import Float164
from my_msgs.msg import Int164
from my_msgs.msg import String4
# from my_msgs.msg import Carcontrol1

# msg = String4()
class KeyPublisher(Node):

    def __init__(self):
        super().__init__('key_pub')
        self.pub = self.create_publisher(String4, 'key', 10)
        self.msg = String4()
        self.i = 0

    def key_pub(self):
        
        # msg.data = 'Hello World: %d' % self.i
        # print('def1')
        self.msg.one = input('문자를 입력하세요 :')
        # print('def2')
        self.pub.publish(self.msg)

        self.i += 1



def main(args=None):
    rclpy.init(args=args)

    Key_Publisher = KeyPublisher()

    while True:
        Key_Publisher.key_pub()
        Key_Publisher.get_logger().info('Publishing: "%s"' % Key_Publisher.msg.one)

    Key_Publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
