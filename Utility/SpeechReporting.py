from gtts import gTTS
from pygame import mixer
import time
import os

def speechReporting(text_value):
    text2speech = gTTS(text=text_value, lang='en')
    text2speech.save("report.mp3")
    mixer.init()
    mixer.music.load("report.mp3")
    mixer.music.play()
    time.sleep(5)
    mixer.music.stop()
    mixer.quit()