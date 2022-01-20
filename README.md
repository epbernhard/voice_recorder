# A simple voice recorder.

## Script example for a voice sample of 3 seconds, which is saved as "sample.wav".

from voice_recorder import v_rec

length = 3 #(seconds)\
fps = 44100 #(frames per seconds)

voice_recorder = v_rec.Recorder(length, fps)\
voice_recorder.record()\
voice_recorder.save(name = 'sample')

## Install
git clone https://github.com/epbernhard/voice_recorder.git \
pip install voice_recorder

## Versions
V1.0.1