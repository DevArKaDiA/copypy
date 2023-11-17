import sys
from copypy.copypy import transcribe_video

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <video_path> <output_path>")
        sys.exit(1)
    transcribe_video(sys.argv[1], sys.argv[2])
