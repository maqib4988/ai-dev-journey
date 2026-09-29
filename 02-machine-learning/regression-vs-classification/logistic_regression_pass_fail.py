import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

rng = np.random.default_rng(42)

# 40 students, random study hours between 0.5 and 10
hours = rng.uniform(0.5, 10, size=40).reshape(-1, 1)

# Pass (1) if hours plus some randomness exceeds ~4.5, otherwise fail (0)
passed = (hours.ravel() + rng.normal(0, 1.2, size=40) > 4.5).astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    hours, passed, test_size=0.25, random_state=42, stratify=passed
)

clf = LogisticRegression()
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)
print("Actual:   ", y_test)
print("Predicted:", predictions)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")

# Single prediction
label = clf.predict([[4.5]])[0]
print(f"4.5 hours -> {'Pass' if label == 1 else 'Fail'}")

# Confidence, not just the final answer
proba = clf.predict_proba([[4.5]])[0]
print(f"P(fail) = {proba[0]:.2f}, P(pass) = {proba[1]:.2f}")
