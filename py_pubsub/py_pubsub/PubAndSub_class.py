# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
import numpy as np
from rclpy.node import Node

from std_msgs.msg import String

from my_msgs.msg import Float164
from my_msgs.msg import Int164
from my_msgs.msg import String4
from my_msgs.msg import Carcontrol1

callback_check = 0
control_msg = Carcontrol1()


class ControlSubscriber(Node):
    def __init__(self):
        super().__init__('PubAndSub_sub')
        self.sub = self.create_subscription(String4, 'key', self.key_sub_callback, 10)
        self.sub_msg = String4()
        self.con_msg = Carcontrol1()
        # print('init1')


    def key_sub_callback(self, key):
        self.sub_msg = key #?
        # print('call1')
        
        if self.sub_msg.one == 's':
            self.con_msg.emergency = True
        elif self.sub_msg.one == 'w':
            self.con_msg.emergency = False


class ControlPublisher(Node):
    def __init__(self):
        super().__init__('PubAndSub_pub')
        self.pub = self.create_publisher(Carcontrol1, 'control', 10)

        
    def key_pub(self, msg):
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    # node = rclpy.create_node('PubAndSub.py')
    # sub_key = node.create_subscription(String4, 'key', key_sub_callback, 10)
    # pub_control = node.create_publisher(Carcontrol1, 'control', 10)
    Control_Subscriber = ControlSubscriber()
    Control_Publisher = ControlPublisher()

    i = 0
    while True:
        rclpy.spin_once(Control_Subscriber)

        i += 1
        Control_Publisher.key_pub(Control_Subscriber.con_msg)
        Control_Publisher.get_logger().info('%d Publishing: emergency:%d  speed:%d steer:%d' %(i, Control_Subscriber.con_msg.emergency, Control_Subscriber.con_msg.speed, Control_Subscriber.con_msg.steer))

    rclpy.shutdown()


if __name__ == '__main__':
    main()
