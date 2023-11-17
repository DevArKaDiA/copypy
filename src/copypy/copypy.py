from typing import BinaryIO, cast
from pydub import AudioSegment
import speech_recognition


def extract_audio(video_path) -> BinaryIO:
    # Load the video file
    video = AudioSegment.from_file(video_path, format="mp4")
    audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2)
    return audio.export(format="wav")


def extract_text(audio: BinaryIO) -> str:
    # Load the audio file
    r = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(audio) as source:
        audio_data = r.record(source)
    return r.recognize_whisper(audio_data, language="spanish")


def transcribe_video(video_path: str, output_path: str):
    audio = extract_audio(video_path)
    text = extract_text(audio)
    with open(output_path, "w") as file:
        file.write(text)
