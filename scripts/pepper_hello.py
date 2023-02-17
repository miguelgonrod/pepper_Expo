import rospy
from std_msgs.msg import String
from naoqi_bridge_msgs.msg import SpeechWithFeedback

def hello_callback(data):
        speech = SpeechWithFeedback()
        speech.text = "Hello"
        pub = rospy.Publisher('/speech', SpeechWithFeedback, queue_size=10)
        pub.publish(speech)

rospy.init_node('hello_node', anonymous=True)
rospy.Subscriber("/hello", String, hellocallback)
rospy.spin()
