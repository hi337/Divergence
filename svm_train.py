import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

# Load labeled data from the CSV file
data_df = pd.read_csv('labeled_data.csv')

# Split the data into features (X) and labels (y)
X = data_df[['E_alpha', 'E_beta', 'E_theta', 'E_delta', 'R']]
y = data_df['Label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize SVM classifier with a polynomial kernel (you can experiment with other kernels)
svm_classifier = SVC(kernel='poly', degree=3)  # 3rd-degree polynomial kernel

# Train the SVM classifier
svm_classifier.fit(X_train, y_train)

# Save the trained SVM model
joblib.dump(svm_classifier, 'svm_model.joblib')

# Make predictions on the test set
y_pred = svm_classifier.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Training Accuracy: {accuracy * 100:.2f}%')
