from moviepy.editor import VideoFileClip
from pydub import AudioSegment, silence
# from fuzzywuzzy import fuzz
import rapidfuzz as fuzz
import speech_recognition as sr
import pysrt
import os

# Load the video file and convert it to an audio file
clip = VideoFileClip("The.Sopranos.S05E01.DD5.1.720p.HDTV.x264-g8128.mkv")
clip.audio.write_audiofile("sample.wav")


print("Audio file created")
# Detect silence and split the audio into chunks
audio = AudioSegment.from_file("sample.wav")
nonsilent_chunks = silence.split_on_silence(audio, min_silence_len=1000, silence_thresh=-32)
print("Audio file split into chunks")


# Create a speech recognizer
recognizer = sr.Recognizer()

# Load the subtitle file
subs = pysrt.open('The Sopranos - 4x01 - For All Debts Public and Private.en.srt')

# Iterate over each chunk
for i, chunk in enumerate(nonsilent_chunks):
    print(f"Processing chunk {i}")
    # Save chunk to a temporary file
    chunk.export("chunk.wav", format="wav")

    with sr.AudioFile('chunk.wav') as source:
        # Read the audio file
        audio = recognizer.record(source)

        # Use Google Web Speech API to recognize the speech
        try:
            result = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            result = ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        # Compare result with subtitle text using fuzzy matching
        if i < len(subs):
            ratio = fuzz.ratio(result, subs[i].text)
            if ratio < 70:  # You may need to adjust this threshold
                print(f"Discrepancy found at chunk {i}:")
                print(f"Speech recognition result: {result}")
                print(f"Subtitle text: {subs[i].text}")
                print(f"Matching ratio: {ratio}")

# Remove temporary file
os.remove("chunk.wav")
os.remove("sample.wav")
