from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    filename = "speech.mp3"
    tts.save(filename)
    os.system(f"start {filename}")

if __name__ == "__main__":
    #text = "Hello, Eric"
    #text = "Hello, Kenadie"
    #text = "Hello, Thalin"
    #text = "Hello, Ryland"
    text = "Hello, Tarrence"
    text_to_speech(text)
