import os
import pandas as pd

# Folder containing CSV files
folder_path = 'data'

# Iterate through CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        # Load the CSV file
        data_df = pd.read_csv(file_path)

        # Check if the filename contains the word "distracted"
        if 'distracted' in filename.lower():
            # Update the 'Label' column to 0
            data_df['Label'] = 0

        # Save the updated DataFrame back to the CSV file
        data_df.to_csv(file_path, index=False)

print("Label updates completed.")
