import sys
from time import sleep
from pydub import AudioSegment
from pydub.playback import play

def play_wav(file_path, play_duration, repeat_count):
    try:
        audio = AudioSegment.from_file(file_path)

        # Trim playback
        play_segment = audio[:play_duration * 1000]

        # Repeat playback
        for i in range(repeat_count):
            print(f"Playing round {i + 1}/{repeat_count}")
            play(play_segment)
            sleep(play_duration)  # short gap to avoid overlap
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Invalid input format. Please try again.")
        print("Example Usage: python playsound.py <filename.wav> <play_duration_seconds> <repeat_count>")
    else:
        file_path = sys.argv[1]
        play_duration = int(sys.argv[2])
        repeat_count = int(sys.argv[3])
        play_wav(file_path, play_duration, repeat_count)
