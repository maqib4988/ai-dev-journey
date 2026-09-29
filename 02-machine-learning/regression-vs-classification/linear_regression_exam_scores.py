import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Same data as the scatter plot
rng = np.random.default_rng(42)
hours = np.arange(1, 10.5, 0.5).reshape(-1, 1)  # features must be 2D
scores = 45 + 5.5 * hours.ravel() + rng.normal(0, 3, size=len(hours))
scores = np.clip(scores, 0, 100)

# 1. Split
X_train, X_test, y_train, y_test = train_test_split(
    hours, scores, test_size=0.25, random_state=42
)

# 2. Create the model (untrained)
model = LinearRegression()

# 3. Train it
model.fit(X_train, y_train)

# 4. Inspect what it learned
print("Slope (points per extra hour):", model.coef_[0])
print("Intercept (score at 0 hours):", model.intercept_)

# 5. Predict on unseen test data
predictions = model.predict(X_test)
for h, actual, pred in zip(X_test.ravel(), y_test, predictions):
    print(f"{h:>4} hrs | actual {actual:6.1f} | predicted {pred:6.1f}")

# 6. Evaluate
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R2 score: {r2:.3f}")

# 7. Predict something brand new
new_score = model.predict([[6.3]])
print(f"Predicted score for 6.3 hours: {new_score[0]:.1f}")
