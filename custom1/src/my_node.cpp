#include <cstdio>
#include "std_msgs/msg/string.hpp"

#include "rclcpp/rclcpp.hpp"


#include "my_msgs/msg/carcontrol1.hpp"
#include "my_msgs/msg/float164.hpp"
#include "my_msgs/msg/int164.hpp"
#include "my_msgs/msg/string4.hpp"


int main(int argc, char ** argv)
{
  (void) argc;
  (void) argv;

  printf("hello world my_package package\n");
  return 0;
}
