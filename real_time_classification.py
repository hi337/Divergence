from muselsl import stream
import numpy as np
import joblib

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

# Load the trained SVM model
svm_model = joblib.load('svm_model.joblib')

# Connect to the Muse headset and start streaming
stream_process = stream()
stream_process.start()

try:
    # Real-time classification
    while True:
        sample, timestamp = stream_process.get_next_sample()
        eeg_sample = sample['AF7']
        
        # Process EEG data
        features = process_eeg_data(eeg_sample)
        features_array = np.array([features])

        # Predict attention state using the trained SVM model
        prediction = svm_model.predict(features_array)[0]

        # Print the classification result to the console
        if prediction == 1:
            print("Attentive")
        else:
            print("Inattentive")

finally:
    # Stop streaming when done
    stream_process.stop()
