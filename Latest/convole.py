import librosa
import librosa.display
import soundfile as sf  # For saving audio

# Step 1: Read the wave data from the input files
# Replace 'sa.wav' and 'ni.wav' with the paths to your 'sa' and 'ni' audio files.
audio_sa, sample_rate_sa = librosa.load('C:/Users/vinee/Downloads/Mini/old/consecutive/freqNi.wav')
audio_ni, sample_rate_ni = librosa.load('C:/Users/vinee/Downloads/Mini/old/consecutive/freqSa.wav')

# Step 2 (Optional): Define a convolution kernel
# If you have a specific kernel you want to convolve with, define it here.

# Step 3: Use librosa.effects.preemphasis to perform convolution between the two signals
# Replace 'kernel' with your defined kernel if needed.
convolved_signal = librosa.effects.preemphasis(audio_sa, coef=0.97)

# Step 4: Save the convolved signal to a new wave file
# Replace 'output.wav' with the desired output file name.
sf.write('output.wav', convolved_signal, max(sample_rate_sa, sample_rate_ni))
