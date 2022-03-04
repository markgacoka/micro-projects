import speech_recognition as sr

r = sr.Recognizer()
while True:
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration=1)
		print("Say something!")
		audio = r.listen(source)

	try:
		response = r.recognize_google(audio)
		print("You said : {}".format(response))

	except:
		print("I could not understand audio")
