import whisper

model = whisper.load_model("small")
# result = model.transcribe(r"Adv & accurt model\my_self.mp3")
#for in hindi
result = model.transcribe(r"Adv & accurt model\my_self.mp3", language="en",task="transcribe")
print(result["text"])