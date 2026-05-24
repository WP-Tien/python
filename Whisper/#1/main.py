import sounddevice as sd
from scipy.io.wavfile import write
import whisper

fs = 16000
seconds = 5

print("🎤 Đang ghi âm...")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
write("record.wav", fs, audio)

model = whisper.load_model("base")
result = model.transcribe("record.wav", language="vi")

print("📝 Văn bản:", result["text"])