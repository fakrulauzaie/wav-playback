# wav-playback
A simple Python script that plays a `.wav` audio file with a customizable play duration and repeat count. Uses `pydub` library for the audio processing.

Features:
- Play any .wav file.
- Control the play duration (in seconds).
- Specify the number of repeats.

## Prerequisites
1. Python 3.x
2. Dependencies:
```
pip install pydub simpleaudio
```
If there's no media processor installed, install one.
```
sudo apt install ffmpeg
```

## Usage
Run the script with the following command:
```
python playsound.py <filename.wav> <play_duration_seconds> <repeat_count>
```

### Example
To play the file cantinaband.wav for 2 seconds and repeat it 5 times:
```
python playsound.py cantinaband.wav 2 5
```

If the requested play duration is longer than the audio length, the extra duration will be silent. A warning will be shown in the terminal.

For example:
```
Warning: Requested play duration (6 seconds) is longer than the audio length (4 seconds). The extra duration will be silent.
```

### Parameters
- `<filename.wav>`: Path to the `.wav` file.
- `<play_duration_seconds>`: Duration to play the audio in seconds.
- `<repeat_count>`: Number of times to repeat playback.

