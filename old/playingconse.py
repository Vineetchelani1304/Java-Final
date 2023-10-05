import sounddevice as sd
import os
import time

# Specify the path to the directory containing audio files for each note
audio_path = "C:/Users/vinee/Downloads/Mini/consecutive"

# Define the sargam pairs
sargam_pairs = ['Sa Re Re Ga Ga Ma Ma Pa Pa Dha Dha Ni Ni Sa']

# Specify the number of times to play the sequences
num_iterations = 1

# Play the sargam pairs in a consecutive manner for multiple iterations
for iteration in range(num_iterations):
    for sargam_pair in sargam_pairs:
        notes = sargam_pair.split()

        for note in notes:
            audio_file = os.path.join(audio_path, note + ".wav")  # Assuming each note is stored as a WAV file
            audio_data, sample_rate = sd.read(audio_file)

            sd.play(audio_data, sample_rate)
            sd.wait()  # Wait until the sound finishes playing

        time.sleep(1)  # Wait for a short interval before playing the next pair

    print(f"Iteration {iteration + 1} completed.")

print("All iterations completed.")