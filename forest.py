from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import joblib

# Load the labeled_data.csv file
data_df = pd.read_csv('selected_data.csv')

# Extract 'R' and 'Label' columns
selected_columns = ['R', 'Label']
selected_data = data_df[selected_columns]

# Drop rows with NaN or infinite values in the 'R' column
selected_data = selected_data.replace([np.inf, -np.inf], np.nan).dropna(subset=['R'])

# Extract features and labels
X = selected_data['R'].values.reshape(-1, 1)  # Reshape to ensure X is a 2D array
y = selected_data['Label'].values

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

# Initialize and train the Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)  # You can adjust the number of trees
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_classifier.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save the trained Random Forest model
joblib.dump(rf_classifier, 'random_forest_model_r_value.joblib')
