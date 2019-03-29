#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

velocity_publisher = rospy.Publisher(
    '/robotont/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()


def closing():
    # After the loop, stops the robot
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    # Force the robot to stop
    velocity_publisher.publish(vel_msg)

#######################
# YOUR FUNCTIONS HERE #
#######################
def  func_1(kestus, kiirus):
    #while not rospy.is_shutdown():
        for i in range(0,kestus):
            vel_msg.linear.x = kiirus
            vel_msg.linear.y = 0
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            rospy.sleep(0.3)
def  func_2(kestus, kiirus):
    #while not rospy.is_shutdown():
        for i in range(0,kestus):
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.angular.z = kiirus
            velocity_publisher.publish(vel_msg)
            rospy.sleep(0.3)
def  func_3(kestus, kiirus):
    #while not rospy.is_shutdown():
        for i in range(0,kestus):
            vel_msg.linear.x = 0
            vel_msg.linear.y = kiirus
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            rospy.sleep(0.3)
   
###########################
# YOUR FUNCTIONS HERE END #
###########################


def move():
    # Starts a new node
    rospy.init_node('robotont_velocity_publisher', anonymous=True)

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        ########################
        # YOUR CODE HERE START #
        ########################
        #vel_msg.linear.x = 0
        #vel_msg.linear.y = 0
        #vel_msg.angular.z = 0
        #velocity_publisher.publish(vel_msg)
        #rospy.sleep(0.1)
        func_1(10,0.3)
        func_2(13,0.48)
        #func_3(20,-0.2)
        #func_3(10,0.2)
        func_1(10,0.3)
        func_2(13,-0.48)
        func_1(10,0.3)
        func_2(13,-0.48)
        ######################
        # YOUR CODE HERE END #
        ######################


if __name__ == '__main__':
    try:
        rospy.on_shutdown(closing)
        move()
    except rospy.ROSInterruptException:
        pass
