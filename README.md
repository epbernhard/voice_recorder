# A simple voice recorder.

## Example on a mini voice sample of 3 seconds, which is saved as "yes.wav" (i.e. assuming you are recording a yes).

NAME = 'yes'\
TIME_S = 3\
F_S = 44100

voice_recorder = Recorder(TIME_S, F_S)\
voice_recorder.record()

voice_recorder.playback()  (If you want to play back the sample)

write(NAME+".wav", F_S , voice_recorder.sample)

## Libraries
NumPy, sounddevice, scipy, tqdm, and time.

## Versions
V1.0.0