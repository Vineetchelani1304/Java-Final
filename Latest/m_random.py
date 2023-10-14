import random
import numpy as np
import sounddevice as sd
import time

def m():
    # Define the musical scale (C major scale in this example)
    scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

    # Define the length of the melody (number of notes)
    melody_length = 10  # You can adjust this to your desired length


    # Create a pleasant-sounding envelope
    def envelope(note_duration_ms, sample_rate):
        attack = int(note_duration_ms * 0.1 * sample_rate / 1000)
        decay = int(note_duration_ms * 0.2 * sample_rate / 1000)
        sustain = int(note_duration_ms * 0.6 * sample_rate / 1000)
        release = int(note_duration_ms * 0.1 * sample_rate / 1000)

        envelope = np.concatenate((
            np.linspace(0, 1, attack),
            np.linspace(1, 0.6, decay),
            np.full(sustain, 0.6),
            np.linspace(0.6, 0, release)
        ))
        return envelope


    # Generate a random melody
    random_melody = []

    for _ in range(melody_length):
        # Randomly select a note from the scale
        random_note = random.choice(scale)
        random_melody.append(random_note)

    # Define note duration in milliseconds and sample rate
    note_duration_ms = 500
    sample_rate = 44100

    # Generate and play notes in the melody
    for note in random_melody:
        # Frequency mapping for the C major scale
        note_freqs = {
            'C': 261.63,
            'D': 293.66,
            'E': 329.63,
            'F': 349.23,
            'G': 392.00,
            'A': 440.00,
            'B': 493.88,
        }

        frequency = note_freqs.get(note, 0)  # Set to 0 if the note is not found in the dictionary

        if frequency > 0:
            t = np.linspace(0, note_duration_ms / 1000, int(note_duration_ms * sample_rate / 1000), endpoint=False)
            sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)
            envelope_wave = envelope(note_duration_ms, sample_rate) * sine_wave

            # Play the note
            sd.play(envelope_wave, sample_rate)
            sd.wait()
        else:
            # If the note is not found, pause for the note duration
            time.sleep(note_duration_ms / 1000)

    # Wait for the melody to finish playing
    time.sleep(1)  # Adjust this to ensure the last note finishes playing before the program exits