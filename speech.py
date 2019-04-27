import speech_recognition as sr

reach = sr.Recognizer()

harvad=sr.AudioFile('taunt.wav')
with harvad as source:
    audio = reach.record(source)
string = reach.recognize_google(audio)
print(string)

binary = ' '.join(format(ord(x), 'b') for x in string)
print(binary,end='\n')