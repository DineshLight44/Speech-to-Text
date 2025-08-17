import scipy.io.wavfile as wav
from python_speech_features import mfcc

rate, sig = wav.read(r"Audio Preprocessing\output.wav")
mfcc_features = mfcc(sig, rate)
print(mfcc_features)