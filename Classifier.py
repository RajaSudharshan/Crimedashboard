import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Connect to the SQLite database
conn = sqlite3.connect('mlmodels/db.sqbpro')

# Define the SQL query to load the data
query = '''
SELECT AccusedName, Sex, FIRNo, Age, CriminalBehavior
FROM accused_dataset
'''

# Load the data from the database into a Pandas DataFrame
accused_data = pd.read_sql_query(query, conn)

# Define relevant features for prediction
features = ['AccusedName', 'Sex', 'FIRNo']

# Encode categorical variables
label_encoders = {}
for column in ['AccusedName', 'Sex']:
    label_encoders[column] = LabelEncoder()
    accused_data[column] = label_encoders[column].fit_transform(accused_data[column])

# Split data into features (X) and target (y)
X = accused_data[features]
y = accused_data['CriminalBehavior']

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

# Predict criminal behavior
y_pred = rf_classifier.predict(X_test_preprocessed)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Display classification report
print(classification_report(y_test, y_pred))

# Optionally, you can save the trained model for future use
# import joblib
# joblib.dump(rf_classifier, 'criminal_behavior_prediction_model.pkl')

# Close the database connection
conn.close()