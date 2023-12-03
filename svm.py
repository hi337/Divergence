from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

# Load the combined and shuffled data
data_df = pd.read_csv('labeled_data.csv')

# Extract features and labels
X = data_df.drop('Label', axis=1).values
y = data_df['Label'].values

# Check for NaN values
nan_indices = np.isnan(X).any(axis=1)

# Check for infinite values
inf_indices = np.isinf(X).any(axis=1)

# Print problematic indices
print("NaN indices:", np.where(nan_indices)[0])
print("Infinite indices:", np.where(inf_indices)[0])

# Handle NaN and infinite values
X[np.isnan(X)] = 0
X[np.isinf(X)] = np.finfo(np.float64).max

# Check data types
print("Data type of X before scaling:", X.dtype)

# Scale features to the range [0, 1]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Set data type to np.float64
X_scaled = X_scaled.astype(np.float64)

# Check data types after scaling
print("Data type of X after scaling:", X_scaled.dtype)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize and train the SVM classifier
svm_classifier = SVC(kernel='poly', degree=3, gamma='scale')  # You can adjust the kernel as needed
svm_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = svm_classifier.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
