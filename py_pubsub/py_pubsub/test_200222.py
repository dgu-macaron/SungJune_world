import rclpy

from std_msgs.msg import String

from my_msgs.msg import Float164
from my_msgs.msg import Int164
from my_msgs.msg import String4
# from my_msgs.msg import Carcontrol1




def main(args=None):
    a = String4()
    b = String4()
    # a.one = 'a'
    # b.one = 'a'
    if a == b:
        print ('Same')
    else:
        print ('Diffrent')


if __name__ == '__main__':
    main()
