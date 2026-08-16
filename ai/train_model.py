import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ==========================================
# Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "gesture_dataset.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "ai",
    "gesture_model.pkl"
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    "ai",
    "label_encoder.pkl"
)

# ==========================================
# Load Dataset
# ==========================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(DATASET_PATH)
print(df["label"].value_counts())

print(f"Samples : {len(df)}")
print(f"Columns : {len(df.columns)}")

# ==========================================
# Features and Labels
# ==========================================

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

print("\nDetected Gesture Classes:")
print(sorted(y.unique()))

# ==========================================
# Encode Labels
# ==========================================

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

print("\nLabel Mapping")

for i, name in enumerate(encoder.classes_):
    print(f"{i} -> {name}")

# ==========================================
# Train/Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ==========================================
# Train Model
# ==========================================

print("\nTraining Random Forest Model...")

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("Training Complete.")

# ==========================================
# Evaluation
# ==========================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)

print(f"Accuracy : {accuracy * 100:.2f}%")

print("\nClassification Report\n")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=encoder.classes_
    )
)

print("Confusion Matrix\n")

print(confusion_matrix(y_test, y_pred))

# ==========================================
# Save Model
# ==========================================

joblib.dump(model, MODEL_PATH)
joblib.dump(encoder, ENCODER_PATH)

print("\n" + "=" * 60)
print("FILES SAVED")
print("=" * 60)

print("Model Saved To:")
print(MODEL_PATH)

print()

print("Label Encoder Saved To:")
print(ENCODER_PATH)

print("\nTraining Finished Successfully.")