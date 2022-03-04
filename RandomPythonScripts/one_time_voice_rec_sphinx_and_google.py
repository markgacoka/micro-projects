import speech_recognition as sr
#import pyaudio

r = sr.Recognizer()
with sr.Microphone() as source:
	print("Listening")
	r.adjust_for_ambient_noise(source, duration=0.5)
	audio = r.listen(source, timeout=5, phrase_time_limit=3)

try:
	text = r.recognize_sphinx(audio)
#	text = r.recognize_google(audio)
	print("You said " + text)
except:
	print("Translation failed")
