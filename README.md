# A simple voice recorder.

Example on a mini sample of 3 seconds which records "yes":

time_s = 3
fs = 44100

voice_recorder = recorder(time_s, fs)
voice_recorder.record()
yes = voice_recorder.sample

If you want to play back what you just said use:
voice_recorder.playback()

To save the file, use:
write("yes.wav", fs , yes)

Libraries:
NumPy, sounddevice, scipy, tqdm, and time.
