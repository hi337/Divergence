import pandas as pd

# Load the labeled_data.csv file
data_df = pd.read_csv('labeled_data.csv')

# Extract only the 'R' and 'Label' columns
selected_columns = ['R', 'Label']
selected_data = data_df[selected_columns]

# Save the selected data to a new CSV file
selected_data.to_csv('selected_data.csv', index=False)

print("Selected data saved to selected_data.csv")
