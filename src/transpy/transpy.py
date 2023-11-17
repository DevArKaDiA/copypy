from typing import BinaryIO, cast
from pydub import AudioSegment
import sys
import speech_recognition


def extract_audio(video_path, audio_path) -> BinaryIO:
    # Load the video file
    video = AudioSegment.from_file(video_path, format="mp4")
    audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2)
    return audio.export(audio_path, format="wav")


def extract_text(audio: BinaryIO) -> str:
    # Load the audio file
    r = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(audio) as source:
        audio_data = r.record(source)
    return r.recognize_google(audio_data, lenguage="es-ES")


def transcribe_video(video_path: str, output_path: str):
    audio = extract_audio(video_path, "audio.wav")
    text = extract_text(audio)
    with open(output_path, "w") as file:
        file.write(text)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <video_path> <output_path>")
        sys.exit(1)
    transcribe_video(sys.argv[1], sys.argv[2])