import noisereduce as nr
import soundfile as sf ## to read and write audio files 

data, rate = sf.read(r"Audio Preprocessing\output.wav")

clean = nr.reduce_noise(y=data, sr=rate)

sf.write("clean.wav", clean, rate)