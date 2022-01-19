import numpy as np
import sounddevice
from scipy.io.wavfile import write
from tqdm import tqdm
import time

class recorder():

	def __init__(self, sec, fs, sample = []):

		self.sec = sec # Recording time in seconds
		self.fs = fs # Sampling frequency
		self.sample = sample

	def record(self, channels = 2, pgbar = True):
		print("Recording...")
		self.sample = sounddevice.rec(int(self.sec * self.fs ), samplerate = self.fs , channels = channels)
		if pgbar == True:
			[time.sleep(1) for i in tqdm(range(0, self.sec))]
		else:
			sounddevice.wait()
		print("Finished recording.")

	def playback(self):
		if len(self.sample) == 0:
			raise ValueError("Sorry, there is nothing to play back.")
		else:
			sounddevice.play(self.sample, self.fs)


time_s = 3
fs = 44100

voice_recorder = recorder(time_s, fs)
voice_recorder.record()

# If you want to play back what you just said
# voice_recorder.playback()

yes = voice_recorder.sample
write("yes.wav", fs , yes)