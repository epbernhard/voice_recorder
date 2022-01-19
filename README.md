A simple voice recorder.

Example on a mini sample of 3 seconds which records "yes":

time_s = 3
fs = 44100

voice_recorder = recorder(time_s, fs)
print("Recording...")
voice_recorder.record()
print("Finished recording.")

If you want to play back what you just said use:
voice_recorder.playback()

yes = voice_recorder.sample
write("yes.wav", fs , yes)
