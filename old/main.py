import numpy as np
import sounddevice as sd
import random


def generate_sine_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)
    return wave


def play_sound(wave, sample_rate):
    sd.play(wave, sample_rate)
    sd.wait()


def generate_random_frequencies(frequency_list, num_frequencies):
    return random.sample(frequency_list, num_frequencies)


if __name__ == "__main__":
    frequency_list = [65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.83, 110.00, 116.54, 123.47]
    # Frequencies in Hz
    num_frequencies = 3  # Number of random frequencies to play
    duration = 3  # seconds
    sample_rate = 44100  # samples per second

    random_frequencies = generate_random_frequencies(frequency_list, num_frequencies)

    chord_wave = np.zeros(int(duration * sample_rate))
    for freq in random_frequencies:
        sine_wave = generate_sine_wave(freq, duration, sample_rate)
        chord_wave += sine_wave

    play_sound(chord_wave, sample_rate)
