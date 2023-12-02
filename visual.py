from muselsl import stream, list_muses
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate Power Spectral Density (PSD) from FFT result
def calculate_psd(fft_result):
    return np.abs(fft_result) ** 2 / len(fft_result)

# Function to process EEG data and extract features
def process_eeg_data(eeg_data):
    # Apply FFT to transform EEG data to the frequency domain
    fft_result = np.fft.fft(eeg_data)
    
    # Power Spectral Density (PSD) calculation
    psd = calculate_psd(fft_result)
    
    # Define frequency bands
    freq_bands = {
        'alpha': (8, 13),
        'beta': (14, 30),
        'theta': (4, 7),
        'delta': (1, 4)
    }
    
    # Extract features based on waveband distribution
    E_alpha = np.sum(psd[freq_bands['alpha'][0]:freq_bands['alpha'][1]])
    E_beta = np.sum(psd[freq_bands['beta'][0]:freq_bands['beta'][1]])
    E_theta = np.sum(psd[freq_bands['theta'][0]:freq_bands['theta'][1]])
    E_delta = np.sum(psd[freq_bands['delta'][0]:freq_bands['delta'][1]])
    
    return E_alpha, E_beta, E_theta, E_delta

# Connect to the Muse headset and start streaming
muses = list_muses()
stream_process = stream(muses[0]['address'])
stream_process.start()

# Initialize plot
fig, ax = plt.subplots()
x = np.arange(0, 100, 1)  # Assume you want to display the last 100 data points
line, = ax.plot(x, np.zeros_like(x))

# Set plot properties
ax.set_ylim(0, 100)  # Adjust the y-axis limit as needed
ax.set_title('Brainwave Visualization')
ax.set_xlabel('Time')
ax.set_ylabel('Power')

try:
    while True:
        sample, timestamp = stream_process.get_next_sample()
        eeg_sample = sample['AF7']

        # Process EEG data
        E_alpha, E_beta, E_theta, E_delta = process_eeg_data(eeg_sample)

        # Update the plot
        line.set_ydata([E_alpha, E_beta, E_theta, E_delta])
        plt.pause(0.1)  # Pause for a short duration for real-time visualization

except KeyboardInterrupt:
    print("Visualization stopped by user.")

finally:
    # Stop streaming when done
    stream_process.stop()
    plt.close()
