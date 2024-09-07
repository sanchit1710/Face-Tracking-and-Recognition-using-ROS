#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Int32

face_cascade = cv2.CascadeClassifier('/home/sanchit/Downloads/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def main():
    rospy.init_node('face_centroid_publisher', anonymous=True)
    pub = rospy.Publisher("face_centroid_x", Int32, queue_size=10)
    rate = rospy.Rate(10)
     
    while not rospy.is_shutdown():
        ret, img = cap.read()
        if ret:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                centroid_x = x + w // 2
                centroid_y = y + h // 2
                rospy.loginfo(f"Face centroid: ({centroid_x}, {centroid_y})")
                pub.publish(centroid_x)
                cv2.rectangle(img, (x, y), (x+w, y+h), (100, 200, 0), 1)
                cv2.putText(img, 'Harsh', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)
                cv2.circle(img, (centroid_x, centroid_y), 4, (0, 255, 0), -1)
                cv2.putText(img, f'({centroid_x}, {centroid_y})', (centroid_x + 10, centroid_y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 255, 0), 2)
                
            cv2.imshow('21BRS1632', img)
            cv2.waitKey(1)
        rate.sleep()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
