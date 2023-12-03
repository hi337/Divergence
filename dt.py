from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import joblib

# Load the labeled_data.csv file
data_df = pd.read_csv('labeled_data.csv')

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
X_train, X_valid, y_train, y_valid = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree classifier
tree_classifier = DecisionTreeClassifier(random_state=42)
tree_classifier.fit(X_train, y_train)

# Make predictions on the validation set
y_pred_valid = tree_classifier.predict(X_valid)

# Evaluate the accuracy
accuracy_valid = accuracy_score(y_valid, y_pred_valid)
print("Validation Accuracy:", accuracy_valid)

# Save the trained Decision Tree model
joblib.dump(tree_classifier, 'decision_tree_model_r_value.joblib')
