import pygame
import time
import wave
import struct


def play_with_gap_and_save(file1, file2, gap_seconds, output_file):
    # Initialize the pygame mixer
    pygame.mixer.init()

    # Load the WAV files
    sound1 = pygame.mixer.Sound(file1)
    sound2 = pygame.mixer.Sound(file2)

    # Play the first sound
    sound1.play()

    # Wait for the first sound to finish
    while pygame.mixer.get_busy():
        pygame.time.wait(100)

    # Pause for the gap duration
    time.sleep(gap_seconds)

    # Play the second sound
    sound2.play()

    # Wait for the second sound to finish
    while pygame.mixer.get_busy():
        pygame.time.wait(100)

    # Get the audio data and parameters
    audio_data = pygame.mixer.get_raw()
    sample_width = pygame.mixer.get_init()[1] // 8  # Convert bits to bytes
    frame_rate = pygame.mixer.get_init()[0]
    num_channels = 1  # For mono audio

    # Write the combined audio to a new WAV file
    with wave.open(output_file, 'wb') as output_wav:
        output_wav.setnchannels(num_channels)
        output_wav.setsampwidth(sample_width)
        output_wav.setframerate(frame_rate)
        output_wav.writeframes(audio_data)


# WAV file paths
file1 = "C:/Users/vinee/Downloads/Mini/frequency/freq240.wav"
file2 = "C:/Users/vinee/Downloads/Mini/frequency/freq240.wav"

# Gap duration in seconds
gap_seconds = 0.5

# Output WAV file path for combined audio with gap
output_file = "combined_with_gap.wav"

# Play the sounds with a gap and save as a new WAV file
play_with_gap_and_save(file1, file2, gap_seconds, output_file)
