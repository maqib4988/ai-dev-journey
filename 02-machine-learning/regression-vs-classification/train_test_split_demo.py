import numpy as np
from sklearn.model_selection import train_test_split

# 20 samples, 1 feature each
X = np.arange(20).reshape(-1, 1)  # features (2D: rows x columns)
y = np.array([i * 2 + 5 for i in range(20)])  # target (1D)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("X shape:", X.shape)  # (20, 1)
print("Train size:", len(X_train))  # 16
print("Test size:", len(X_test))  # 4
print("Test data:", (X_train))
print("First 3 training rows:", X_train[:3].ravel())
print("Train data:", (y_train))
print("Matching targets:", y_train[:3])
