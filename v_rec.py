"""A simple voice recorder"""
import time
import sounddevice
from scipy.io.wavfile import write
from tqdm import tqdm

class Recorder():
    """Class Recorder containing methods for recording."""

    def __init__(self, sec, f_s, sample = []):
        """Init the class Recorder.

        Parameters:
        sec (float): recording time in seconds.
        f_s (int): numbers of frames.

        Keywords:
        sample (array): array of float containing the recording.
        """

        self.sec = sec # Recording time in seconds
        self.f_s = f_s # Sampling frequency
        self.sample = sample

    def record(self, channels = 2, pgbar = True):
        """Method for the recording.

        Keywords:
        channels (int): the number of recording channels.
        pgbar (bool): whether to display a progress bar while recording.
        """
        print("Recording...")
        self.sample = sounddevice.rec(int(self.sec * self.f_s ), \
                                      samplerate = self.f_s , \
                                      channels = channels)
        if pgbar:
            [time.sleep(1) for i in tqdm(range(0, self.sec))]
        else:
            sounddevice.wait()
        print("Finished recording.")

    def playback(self):
        """Method for the playback."""

        if len(self.sample) == 0:
            raise ValueError("Sorry, there is nothing to play back.")

        sounddevice.play(self.sample, self.f_s)
        sounddevice.wait()

if __name__ == "__main__":

    NAME = 'yes'
    TIME_S = 3
    F_S = 44100

    voice_recorder = Recorder(TIME_S, F_S)
    voice_recorder.record()

    # If you want to play back what you just said
    # voice_recorder.playback()

    write(NAME+".wav", F_S , voice_recorder.sample)
