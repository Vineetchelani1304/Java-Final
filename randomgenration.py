import sounddevice as sd
import numpy as np
import time
import random
from scipy.io.wavfile import write

# Define the frequencies for each note
note_freqs = {
    'sa': 240,
    're': 270,
    'ga': 300,
    'ma': 320,
    'pa': 360,
    'dha': 400,
    'ni': 450,
    'se': 480,
}

# Specify the number of audio files to generate
num_files = 7 ** 4

# Initialize variables for the audio data
sample_rate = 44100  # samples per second
duration = 0.5  # in seconds
t = np.linspace(0, duration, int(sample_rate * duration), False)
'''
# Generate and save multiple audio files
for file_num in range(num_files):
    random_notes = random.choices(list(note_freqs.keys()), k=10)

    audio_data = []
    for note in random_notes:
        frequency = note_freqs[note]
        tone = 0.3 * np.sin(2 * np.pi * frequency * t)
        audio_data.extend(tone)

    # Save the audio data to a WAV file
    file_name = f"C:/Users/vinee/Downloads/Mini/RandomData/Random_Music_{file_num + 1}.wav"
    write(file_name, sample_rate, np.array(audio_data))
    print(f"Finished saving {file_name}")

print("All files generated and saved.")
'''
# Play two consecutive notes in a loop
while True:
    random_notes = random.choices(list(note_freqs.keys()), k=2)

    for note in random_notes:
        frequency = note_freqs[note]
        tone = 0.3 * np.sin(2 * np.pi * frequency * t)
        sd.play(tone, sample_rate)
        sd.wait()  # Wait until the sound finishes playing

    time.sleep(1)  # Wait for a short interval before playing the next set of notes
#silence = np.zeros_like(t)
#sd.play(silence, sample_rate)
#sd.wait()