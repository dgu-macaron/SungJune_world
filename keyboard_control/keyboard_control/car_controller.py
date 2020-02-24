#!/usr/bin/env python

import rclpy, sys
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import numpy as np

key_dict = {
        'w':(  1.0,   0.0,   0.0),
        's':(  0.0,   0.0,   0.0),
        'a':(  0.0,   1.0,   0.0),
        'd':(  0.0,   0.0,   1.0),
      }
speed = 0
steer = 0
sp_stack = 1
st_stack = 1
st_count = 0
zero_sp = 0
key = String()
control_val = Twist()


def callback(data):
    global speed, steer, sp_stack, st_stack, st_count, zero_sp
    key = data


    if key.data in key_dict.keys():
        sp_rate = 1.3
        if (key_dict[key.data][0] or key_dict[key.data][1] or key_dict[key.data][2]) == 0:
            sp_stack = 1
            zero_sp = 0
        elif key_dict[key.data][0] == 1:
            sp_stack = key_dict[key.data][0] * sp_stack * sp_rate + (not(key_dict[key.data][0])) * sp_stack
            zero_sp = 1

        speed = sp_stack * (key_dict[key.data][0] or key_dict[key.data][1] or key_dict[key.data][2]) * zero_sp

        st_count += -key_dict[key.data][1] + key_dict[key.data][2]
        st_stack = (st_count != 0) * (2**(abs(st_count) - 1))
        steer = -(st_count <0) * st_stack + (st_count > 0) * st_stack

    else:
        sp_stack = 1
        speed = 0.0
        steer = 0.0
        st_count = 1
        
        if (key == '\x03'):
            print('publisher stop working')

    control_val.linear.x = speed
    control_val.linear.y = steer

            

    state = 'speed : {:0.4f} , steer : {:0.4f} '.format(speed, steer)
    print(state)



def main(args=None):
    rclpy.init(args=args)


    node = rclpy.create_node('car_controller')
    Control_Subscriber = node.create_subscription(String, 'keyboard', callback, 10)
    assert Control_Subscriber
    Control_Publisher = node.create_publisher(Twist, 'control', 10)
    i = 0

    while True:
        rclpy.spin_once(node)
        Control_Publisher.publish(control_val)
        i += 1
        # node.get_logger().info('%d Publishing: emergency:%d  speed:%d steer:%d' %(i, control_msg.emergency, control_msg.speed, control_msg.steer))
    rclpy.shutdown()


if __name__=='__main__':

    main()


