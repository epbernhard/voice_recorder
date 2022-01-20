# A simple voice recorder.

## Script example for a voice sample of 3 seconds, which is saved as "sample.wav".

from voice_recorder import v_rec\
from scipy.io.wavfile import write

NAME = 'sample'\
TIME_S = 3\
F_S = 44100

voice_recorder = Recorder(TIME_S, F_S)\
voice_recorder.record()

voice_recorder.playback()  (If you want to play back the sample)

write(NAME+".wav", F_S , voice_recorder.sample)

## Install
git clone https://github.com/epbernhard/voice_recorder.git \
pip install voice_recorder \

## Versions
V1.0.0