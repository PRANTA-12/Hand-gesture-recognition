import pandas as pd
from ai.predictor import AIPredictor

print("=" * 50)
print("AI Predictor Test")
print("=" * 50)

# Load the dataset
dataset = pd.read_csv("dataset/gesture_dataset.csv")

# Take the first sample
row = dataset.iloc[0]

# Expected gesture
expected = row["label"]

# Remove the label column
features = row.drop("label").tolist()

# Create predictor
predictor = AIPredictor()

# Convert features into DataFrame
df = pd.DataFrame(
    [features],
    columns=predictor.feature_columns
)

# Predict
prediction = predictor.random_forest.predict(df)[0]

# Confidence
probabilities = predictor.random_forest.predict_proba(df)[0]
confidence = max(probabilities)

print()
print("Expected Gesture :", expected)
print("Predicted Gesture:", prediction)
print(f"Confidence       : {confidence:.2%}")

if prediction == expected:
    print("\n AI Prediction Successful")
else:
    print("\n AI Prediction Failed")