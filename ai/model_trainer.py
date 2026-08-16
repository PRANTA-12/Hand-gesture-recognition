import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


class ModelTrainer:

    def __init__(
        self,
        dataset_path="dataset/gesture_dataset.csv",
        model_path="models/gesture_model.pkl"
    ):

        self.dataset_path = dataset_path
        self.model_path = model_path

        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)

    # ---------------------------------------------------
    # Load Dataset
    # ---------------------------------------------------

    def load_dataset(self):

        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(
                f"Dataset not found: {self.dataset_path}"
            )

        data = pd.read_csv(self.dataset_path)

        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]

        return X, y

    # ---------------------------------------------------
    # Train Model
    # ---------------------------------------------------

    def train(self):

        print("=" * 50)
        print("Loading Dataset...")
        print("=" * 50)

        X, y = self.load_dataset()

        print(f"Total Samples : {len(X)}")
        print(f"Total Features: {X.shape[1]}")
        print(f"Classes       : {sorted(y.unique())}")

        print("\nSplitting Dataset...")

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y
        )

        print("Training Random Forest Model...\n")

        model = RandomForestClassifier(
            n_estimators=300,
            random_state=42,
            n_jobs=-1
        )

        model.fit(X_train, y_train)

        print("Training Complete.\n")

        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        print("=" * 50)
        print(f"Accuracy : {accuracy * 100:.2f}%")
        print("=" * 50)

        print("\nClassification Report\n")
        print(classification_report(y_test, predictions))

        print("\nConfusion Matrix\n")
        print(confusion_matrix(y_test, predictions))

        joblib.dump(model, self.model_path)

        print(f"\nModel Saved Successfully!")
        print(f"Location : {self.model_path}")

        return model


if __name__ == "__main__":

    trainer = ModelTrainer()

    trainer.train()