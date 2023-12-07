"""
Predictive Model for Income Classification

This script builds and evaluates a Logistic Regression model to predict income categories based on provided demographic and financial features.

Author: Manoj Kumar Singade
Date: 5/12/2023

Usage:
    python income_prediction_model.py

    Steps:
1. Load dataset from a CSV file.
2. Preprocess the dataset by splitting features and the target variable.
3. Build a Logistic Regression model with a preprocessing pipeline.
4. Split the data into training and testing sets.
5. Fit, predict, and evaluate the model's performance on the test set.



"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import classification_report, accuracy_score

def load_data(file_path):
    """
    Load dataset from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Loaded dataset.
    """
    return pd.read_csv(file_path)

def preprocess_data(data):
    """
    Preprocess the dataset by splitting features and target variable.

    Parameters:
    - data (pd.DataFrame): Input dataset.

    Returns:
    - pd.DataFrame: Features.
    - pd.Series: Target variable.
    """
    features = ['age', 'workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country']
    target = 'income'
    X = data[features]
    y = data[target]
    return X, y

def build_model():
    """
    Build a Logistic Regression model with preprocessing pipeline.

    Returns:
    - sklearn.pipeline.Pipeline: Preprocessing and classification model pipeline.
    """
    numeric_features = ['age', 'capital-gain', 'capital-loss', 'hours-per-week']
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())])

    categorical_features = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])

    model = Pipeline(steps=[('preprocessor', preprocessor),
                            ('classifier', LogisticRegression())])
    return model

def evaluate_model(model, X_train, X_test, y_train, y_test):
    """
    Fit, predict, and evaluate the model's performance.

    Parameters:
    - model (sklearn.pipeline.Pipeline): Preprocessing and classification model pipeline.
    - X_train, X_test (pd.DataFrame): Training and testing features.
    - y_train, y_test (pd.Series): Training and testing target variable.

    Returns:
    None
    """
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Model Evaluation:")
    print(classification_report(y_test, predictions))
    print("Accuracy:", accuracy_score(y_test, predictions))

def main():
    """
    Main function to orchestrate the entire process:
    - Load data from a CSV file.
    - Preprocess the data.
    - Split the data into training and testing sets.
    - Build a logistic regression model with preprocessing.
    - Evaluate the model's performance on the test set.
    """

    # Load data
    file_path = 'your_dataset.csv'  # Replace with your dataset file path
    data = load_data(file_path)
    
    # Preprocess data
    X, y = preprocess_data(data)
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Build model
    model = build_model()
    
    # Evaluate model
    evaluate_model(model, X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()

