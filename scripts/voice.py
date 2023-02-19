import qi
import speech_recognition as sr
from naoqi import ALProxy


# connect to the robot
#session = qi.Session()
#session.connect("tcp://192.168.1.100:9559")

# get the speech recognition service
#speech_service = session.service("ALSpeechRecognition")

# Set the language
#speech_service.setLanguage("English")

# subscribe to the recognized speech
#speech_service.subscribe("MySpeechRecognition")

asr = ALProxy("ALSpeechRecognition", "192.168.1.100", 9559)
asr.pause(True)
asr.setLanguage("English")

vocabulary = ["yes", "no", "please"]
asr.setVocabulary(vocabulary, False)

asr.pause(False)
asr.subscribe("Test_ASR")

# create the speech recognizer
recognizer = sr.Recognizer()

# create the microphone input source
mic = sr.Microphone()

# define the voice commands
commands = {"hello": "/hello", "goodbye": "/goodbye"}

#start the main loop
while True:
        # listen for the voice command
        with mic as source:
                print("Say something")
                audio = recognizer.listen(source)

        # recognize the voice command
        try:
                text = recognizer.recognize_google(audio)
                print("you said: " + text)
                if text in commands:
                        # Publish the corresponding topic
                        session.service("ALMemory").raiseEvent(commands[text], 1)
        except sr.UnknownValueError:
                print("Could not understand audio")
        except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

