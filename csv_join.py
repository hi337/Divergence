import os
import pandas as pd
from sklearn.utils import shuffle

# Folder containing CSV files
folder_path = 'data'

# List to store individual DataFrames
data_frames = []

# Iterate through CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        # Load the CSV file
        data_df = pd.read_csv(file_path)

        # Append the DataFrame to the list
        data_frames.append(data_df)

# Combine all DataFrames into a single DataFrame
combined_data = pd.concat(data_frames, ignore_index=True)

# Shuffle the rows randomly
shuffled_data = shuffle(combined_data)

# Save the combined and shuffled DataFrame to a new CSV file
shuffled_data.to_csv('labeled_data.csv', index=False)

print("Combined and shuffled data saved to labeled_data.csv.")
