from pydub import AudioSegment

mp3_audio = AudioSegment.from_mp3(r"Audio Preprocessing\Recording.mp3")
mp3_audio.export(r"Audio Preprocessing\converted.wav", format="wav")