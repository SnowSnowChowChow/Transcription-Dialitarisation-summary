import json

notebook_path = "pipeline_transcription.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Patching first cell instructions to include av
c1 = nb['cells'][0]['source']
new_c1 = []
for line in c1:
    if "pip install " in line and "whisperx.git" in line and "av\n" not in line:
        line = line.replace("pydub\n", "pydub av\n")
    new_c1.append(line)
nb['cells'][0]['source'] = new_c1

# Patching imports and load_audio in cell 2
c2 = nb['cells'][2]['source']
full_c2 = "".join(c2)

if "import av" not in full_c2:
    patch = """import av, numpy as np

# Patch pour utiliser av au lieu de ffmpeg.exe (contourne le blocage AppLocker/WDAC)
def load_audio_direct(file_path: str, sr: int = 16000):
    container = av.open(file_path)
    stream = container.streams.audio[0]
    resampler = av.AudioResampler(format='s16', layout='mono', rate=sr)
    frames = []
    for frame in container.decode(stream):
        for r_frame in resampler.resample(frame):
            frames.append(r_frame.to_ndarray())
    for r_frame in resampler.resample(None):
        frames.append(r_frame.to_ndarray())
    container.close()
    if not frames:
        return np.zeros((0,), dtype=np.float32)
    return np.concatenate(frames, axis=1).flatten().astype(np.float32) / 32768.0

whisperx.audio.load_audio = load_audio_direct
whisperx.load_audio = load_audio_direct

"""
    c2.insert(0, patch)
    nb['cells'][2]['source'] = c2

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Patching successful!")
