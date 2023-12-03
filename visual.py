import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
data_df = pd.read_csv('data\\Jai_concentrated1.csv')

# Plot the features over time
plt.figure(figsize=(10, 6))

# Assuming 'Label' column is present in the CSV file
colors = ['green' if label == 1 else 'red' for label in data_df['Label']]

plt.plot(data_df['E_alpha'], label='Alpha', color='blue')
plt.plot(data_df['E_beta'], label='Beta', color='orange')
plt.plot(data_df['E_theta'], label='Theta', color='green')
plt.plot(data_df['E_delta'], label='Delta', color='purple')
plt.title('Brainwave Features Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Power')
plt.legend()

# # Plot the label over time
# plt.subplot(2, 1, 2)
# plt.scatter(data_df.index, data_df['Label'], color=colors)
# plt.title('Label Over Time')
# plt.xlabel('Time')
# plt.ylabel('Label (1: Attentive, 0: Inattentive)')

plt.tight_layout()
plt.show()
