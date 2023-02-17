from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "192.168.1.100", 9559)
tts.say("Hello, world")
