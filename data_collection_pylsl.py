import pylsl
import numpy as np
import pandas as pd
import time

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
    
    # Calculate the ratio of alpha to beta activities
    R = E_alpha / E_beta
    
    return E_alpha, E_beta, E_theta, E_delta, R

streams = pylsl.resolve_stream('type', 'EEG')
# Connect to the Muse headset using pylsl
inlet = pylsl.StreamInlet(streams[0])

# # Collect EEG data for a certain duration (adjust as needed)
# duration_in_seconds = 10
# eeg_data = []
# labels = []  # 1 for attentive, 0 for inattentive

# start_time = time.time()
# while (time.time() - start_time) < duration_in_seconds:
#     sample, timestamp = inlet.pull_sample()
#     eeg_data.append(sample[:4])  # Assuming AF7 electrode data
#     labels.append(1)
# # Process EEG data
# X = []  # Features
# for eeg_sample in eeg_data:
#     features = process_eeg_data(eeg_sample)
#     X.append(features)
# X = np.array(X)

# # Convert labels to numpy array
# y = np.array(labels)

# # Save data and labels to a CSV file
# data_df = pd.DataFrame(X, columns=['E_alpha', 'E_beta', 'E_theta', 'E_delta', 'R'])
# data_df['Label'] = y
# data_df.to_csv('labeled_data_pylsl.csv', index=False)

while True:    
# get a new sample (you can also omit the timestamp part if you're 
# not interested in it)    
  sample, timestamp = inlet.pull_sample()    
  print(timestamp, sample)