import speech_recognition as sr

recognizer = sr.Recognizer()

# Load audio from file
with sr.AudioFile('output.wav') as source:
    audio = recognizer.record(source)

# Use Google’s online recognizer
text = recognizer.recognize_google(audio)
print(text)
