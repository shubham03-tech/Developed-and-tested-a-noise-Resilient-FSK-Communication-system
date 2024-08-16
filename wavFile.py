import numpy as np
from scipy.io.wavfile import write

duration = 10  
sample_rate = 16000  
amplitude = 0.5  
notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]  

num_samples = duration * sample_rate
num_notes = int(duration * 2)  
song = []

for _ in range(num_notes):
    freq = np.random.choice(notes)
    t = np.linspace(0, 0.5, int(0.5 * sample_rate), endpoint=False)
    note = amplitude * np.sin(2 * np.pi * freq * t)
    song.extend(note)

song = np.array(song)

output_file = "random_song1.wav"
write(output_file, sample_rate, song)
