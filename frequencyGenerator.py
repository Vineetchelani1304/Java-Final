import numpy as np
import soundfile as sf

duration = 5  # seconds
sampling_rate = 44100  # samples per second
frequency = 440  # Hz (frequency of the sine wave)
amplitude = 0.5  # Amplitude of the sine wave

t = np.linspace(0, duration, int(sampling_rate * duration), False)
sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)

# Save the generated sine wave to a WAV file
i=20
while(i<=21):
    file_path = "C:/Users/vinee/Downloads/Mini/testfreq/freq{}.wav".format(frequency)
    sf.write(file_path, sine_wave, sampling_rate)
    print("Sine wave saved to:", file_path)
    frequency=frequency+1
    i=i+1
