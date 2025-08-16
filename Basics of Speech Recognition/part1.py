## How audio is captured in microphone or file and save it
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

duration = 5
fs = 44100

# rec
print("Recording........")
recording = sd.rec(int(duration*fs),samplerate=fs,channels=1,dtype='float32')
sd.wait()
print("recoding finish")

# save to wav file
wav.write("output.wav",fs,(recording*32767).astype(np.int16))
print("Audio save as output.wav")

#play back recoded file
print("playing back")
sd.play(recording,fs)
sd.wait()
print("playback finish")