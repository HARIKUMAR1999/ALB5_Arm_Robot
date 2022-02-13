!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState

joint_publisher = rospy.Publisher('/custom_joint_states', JointState, queue_size=10)
joint = JointState()
joint.name = ["base", "shoulder", "elbow", "wrist", "wrist_twist", "gripper"]
joint.position = [0, 0, 0, 0, 0, 0]

def move0():
    global joint
    joint.position[0] = 0
    joint.position[1] = 0
    joint.position[2] = 0
    joint.position[3] = 0
    joint.position[4] = 0
    joint.position[5] = 0


    joint_publisher.publish(joint)
    rospy.sleep(1)


def movea():
    global joint
    i=0
    joint.position[5] = 0

    while(i<32):
        if(i==31):
            joint.position[5]=1.3
            rospy.sleep(1)
        joint.position[1]-=0.01
        joint.position[3]-=0.033
        joint_publisher.publish(joint)
        rospy.sleep(0.1)
        i+=1


def moveb():
    global joint
    i=0
    #joint.position[5] = 0

    while(i<32):
        if(i==31):
            joint.position[5] = 0
            rospy.sleep(1)
        joint.position[1]+=0.01
        joint.position[3]+=0.033
        joint_publisher.publish(joint)
        rospy.sleep(0.1)
        i+=1



if __name__ == '__main__':
    rospy.init_node('Movement')
    try:
        move0()
        while not rospy.is_shutdown():
            movea()
            moveb()


    except rospy.ROSInterruptException:
        pass