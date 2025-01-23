import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import joblib

# Train the model
def train_model(df, model_path):
    # Define features and target
    X = df[["Temperature", "Run_Time"]]
    y = df["Downtime_Flag"]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # Save the model
    joblib.dump(model, model_path)
    
    return {"accuracy": round(accuracy, 2), "f1_score": round(f1, 2)}

# Make a prediction
def make_prediction(model_path, input_data):
    # Load the model
    model = joblib.load(model_path)
    
    # Convert input data to DataFrame
    X = pd.DataFrame([input_data])
    
    # Predict and get confidence
    probabilities = model.predict_proba(X)[0]
    prediction = model.predict(X)[0]
    confidence = max(probabilities)
    
    return prediction, round(confidence, 2)
