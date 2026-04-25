import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Dummy dataset
data = {
    "f1": [0, 1, 0, 1],
    "f2": [1, 0, 1, 0],
    "f3": [0, 1, 1, 0],
    "f4": [34, 12, 45, 23],
    "f5": [12, 23, 34, 45],
    "f6": [0, 1, 0, 1],
    "label": ["normal", "attack", "attack", "normal"]
}

df = pd.DataFrame(data)

X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved!")