#!/usr/bin/env python

import sys
import copy
import rospy
from std_msgs.msg import Float64

class OpenDogControl(object):
    def __init__(self):

        print "============ Starting"
        rospy.init_node('test_move_opendog', anonymous=True)
        self.last_pos = 0
        self.initPublishers()
        self.move()



    def initListeners(self):
        rospy.Subscriber("/opendog/rf_upperleg_position_controller/state", Float64, callback)
        
    def initPublishers(self):
        self.pubrfu = rospy.Publisher('/opendog/rf_upperleg_position_controller/command', Float64, queue_size=10)
        self.pubrfl = rospy.Publisher('/opendog/rf_lowerleg_position_controller/command', Float64, queue_size=10)
        self.pubrfh = rospy.Publisher('/opendog/rf_hip_position_controller/command', Float64, queue_size=10, latch="true")
        
        self.publfu = rospy.Publisher('/opendog/lf_upperleg_position_controller/command', Float64, queue_size=10)
        self.publfl = rospy.Publisher('/opendog/lf_lowerleg_position_controller/command', Float64, queue_size=10)
        self.publfh = rospy.Publisher('/opendog/lf_hip_position_controller/command', Float64, queue_size=10, latch="true")
        
        self.pubrbu = rospy.Publisher('/opendog/rb_upperleg_position_controller/command', Float64, queue_size=10)
        self.pubrbl = rospy.Publisher('/opendog/rb_lowerleg_position_controller/command', Float64, queue_size=10)
        self.pubrbh = rospy.Publisher('/opendog/rb_hip_position_controller/command', Float64, queue_size=10, latch="true")

        self.publbu = rospy.Publisher('/opendog/lb_upperleg_position_controller/command', Float64, queue_size=10)
        self.publbl = rospy.Publisher('/opendog/lb_lowerleg_position_controller/command', Float64, queue_size=10)
        self.publbh = rospy.Publisher('/opendog/lb_hip_position_controller/command', Float64, queue_size=10, latch="true")
    

    def move(self):
        self.pubrfh.publish(-0.2)
        self.publfh.publish(0.2)
        self.pubrbh.publish(-0.2)
        self.publbh.publish(0.2)
        rospy.sleep(0.2)
        for i in range(0, 10):
            for x in range(0, 400):
                print "We're on time %d" % (x)
                if self.last_pos > 0.2:
                    self.last_pos = 0.2
                pos = self.last_pos + 0.001
                self.pubrfu.publish(pos)
                self.publfu.publish(pos)
                self.pubrbu.publish(pos)
                self.publbu.publish(pos)

                self.pubrfl.publish(pos)
                self.publfl.publish(pos)
                self.pubrbl.publish(pos)
                self.publbl.publish(pos)

                
                self.last_pos = pos 
                rospy.sleep(0.007)
            rospy.sleep(2)
            for x in range(0, 400):
                print "We're on time %d" % (x)
                pos = self.last_pos - 0.001
                self.pubrfu.publish(pos)
                self.publfu.publish(pos)
                self.pubrbu.publish(pos)
                self.publbu.publish(pos)

                self.pubrfl.publish(pos)
                self.publfl.publish(pos)
                self.pubrbl.publish(pos)
                self.publbl.publish(pos)


                
                self.last_pos = pos 
                rospy.sleep(0.005)
        


    
        
if __name__ == '__main__':
    x = OpenDogControl()
    
   