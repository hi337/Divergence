from pylsl import StreamInlet, resolve_stream
import numpy as np
import joblib
import time
import math

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
    E_alpha = psd[0]
    E_beta = psd[1]
    E_theta = psd[2]
    E_delta = psd[3]
    
    # Calculate the ratio of alpha to beta activities
    R = E_alpha / E_beta
    
    return E_alpha, E_beta, E_theta, E_delta, R

# Load the trained SVM model
gb_model = joblib.load('gradient_boosting_model.joblib')

# Resolve an EEG stream from Muse headset using pylsl
streams = resolve_stream('type', 'EEG')
inlet = StreamInlet(streams[0])

# Function to conduct a 60-second test for a specific learning modality
def conduct_learning_test(modality):
    print(f"Conducting {modality} learning test...")
    
    # Variables for collecting data over 60 seconds
    duration = 60  # in seconds
    start_time = time.time()
    data_points = []

    try:
        # Collect data over 60 seconds
        while time.time() - start_time < duration:
            # Get a chunk of EEG data
            sample, timestamp = inlet.pull_sample()
            eeg_sample = sample[:4]  # Assuming the first 4 channels correspond to AF7, AF8, TP9, and TP10
            
            # Process EEG data
            features = process_eeg_data(eeg_sample)
            features_array = np.array([features])

            # Predict attention state using the trained SVM model
            prediction = gb_model.predict(features_array)[0]

            # Collect data points
            data_points.append(prediction)

        # Calculate and print the average value
        average_value = np.mean(data_points)
        print(f"Average Attention Level for {modality} learning test:", average_value)

        return math.ran

    finally:
        # Stop streaming when done
        inlet.close_stream()

# Conduct separate tests for different learning modalities
reading = conduct_learning_test("Reading")
visual = conduct_learning_test("Visual")
auditory = conduct_learning_test("Auditory")
kinesthetic = conduct_learning_test("Kinesthetic")

order_arr = ["reading", "visual", "auditory", "kinesthetic"]
strat_arr = [reading, visual, auditory, kinesthetic]

best = max(strat_arr)
name_of_best = order_arr[strat_arr.index(best)]

print(f"You are a {name_of_best} learner, you were engaged {round((best*100), 2)}% of the time!")

if name_of_best == "reading":
    print("To study optimally, you would benefit greatly from reading books and text material.")
elif name_of_best == "visual":
    print("To study optimally, you would benefit greatly from watching videos and presentations.")
elif name_of_best == "auditory":
    print("To study optimally, you would benefit greatly from listening to lectures and communicating with others.")
else:
    print("To study optimally, you would benefit greatly from using your hands and building projects.")

if strat_arr[0] < 0.4:
    print("You should consult a medical professional to be tested for dyslexia or dysgraphia")
if strat_arr[1] < 0.4:
    print("You should consult a medical professional to be tested for visual processing disorder")
if strat_arr[2] < 0.4:
    print("You should consult a medical professional to be tested for central auditory processing disorder")
if sum(strat_arr) < 0.4:
    print("You should consult a medical professional to be tested for ADHD or Autism")
