import speech_recognition as sr

r = sr.Recognizer()

test_aud = sr.AudioFile('test.wav')
with test_aud as source:
	audio = r.record(source)

text = r.recognize_google(audio)
print(text)