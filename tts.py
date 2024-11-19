import gtts
import playsound
text = input("write something here: ")
sound = gtts.gTTS(text,lang="en-us")
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")