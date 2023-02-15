import pyttsx3

text = ""
filename = input("filename: ")
with open(filename, 'r') as file:
	for i in file:
		text = text + f"\n{i}"

en = pyttsx3.init()
en.say(text)
en.runAndWait()
