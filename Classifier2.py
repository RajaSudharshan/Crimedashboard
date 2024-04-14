import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Load the victim dataset
victim_data = pd.read_csv('victim_info_dataset.csv', encoding='latin-1')

# Define the target variable 'InjuryType' based on criteria
# For example, we'll assume victims with 'InjuryType' containing 'Serious' are considered severe injuries
victim_data['SevereInjury'] = victim_data['InjuryType'].str.contains('Physical').astype(int)

# Select relevant features for prediction
features = ['Age', 'Sex', 'Profession', 'PresentCity', 'PresentState']   # Add more features as needed

# Encode categorical variables
label_encoders = {}  # Define the label_encoders dictionary
for column in ['Sex', 'Profession', 'PresentCity', 'PresentState']:
    label_encoders[column] = LabelEncoder()
    victim_data[column] = label_encoders[column].fit_transform(victim_data[column])

# Split data into features (X) and target (y)
X = victim_data[features]  # Features
y = victim_data['SevereInjury']  # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define preprocessing pipeline
preprocessing_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median'))
])

# Preprocess the data
X_train_preprocessed = preprocessing_pipeline.fit_transform(X_train)
X_test_preprocessed = preprocessing_pipeline.transform(X_test)

# Train a Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train_preprocessed, y_train)

# Predict severe injuries
y_pred = rf_classifier.predict(X_test_preprocessed)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Display classification report
print(classification_report(y_test, y_pred))

# Optionally, you can save the trained model for future use
# import joblib
# joblib.dump(rf_classifier, 'severe_injury_prediction_model.pkl')
