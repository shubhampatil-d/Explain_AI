from gtts import gTTS
import os

def text_to_speech(text, output_file="assets/audio/output.mp3"):
    tts = gTTS(text)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    tts.save(output_file)
    return output_file


# from gtts import gTTS
# import os

# def text_to_speech(text, output_path="assets/audio/output.mp3"):
#     # Convert the cleaned text to speech
#     tts = gTTS(text=text, lang='en')
#     tts.save(output_path)
#     return output_path
