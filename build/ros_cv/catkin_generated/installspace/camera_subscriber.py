#!/usr/bin/env python 3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
def callbackFunction(message):
	bridgeObject=CvBridge()
	rospy.loginfo("received frame")
	convertedFrameBacktoCV=bridgeObject.imgmsg_to_cv2(message)
	cv2.imshow("camera",convertedFrameBacktoCV)
	cv2.waitKey(1)
rospy.init_node('camera_sensor_subscriber',anonymous=True)
rospy.Subscriber('video_topic',Image,callbackFunction)
rospy.spin()
cv2.destroyAllWindows()
