import numpy as np
import sounddevice as sd
from scipy.io import wavfile

def generate(fre):
    # Define parameters
    sample_rate = 44100  # Samples per second
    duration = 5  # Duration in seconds
    freq = fre  # Frequency in Hertz (e.g., A4 note)

    # Generate a time array
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Generate a sine wave with the specified frequency
    audio_data = 0.5 * np.sin(2 * np.pi * freq * t)

    # Scale to 16-bit PCM format (-32768 to 32767)
    audio_data = np.int16(audio_data * 32767)
    sd.play(audio_data, sample_rate)

    # Wait for the audio playback to finish
    sd.wait()

    # Save the audio data as a .wav file
    wavfile.write("audio_frequency2.wav", sample_rate, audio_data)

# Example usage:
#generate(440.0)  # Generates a 440 Hz sine wave and saves it as "audio_frequency2.wav"