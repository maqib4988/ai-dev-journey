import numpy as np
import matplotlib.pyplot as plt

# Reproducible random generator (same seed = same numbers every run)
rng = np.random.default_rng(42)

# 19 students: studied 1 to 10 hours (in 0.5 steps)
hours = np.arange(1, 10.5, 0.5)

# Score = base 45 + 5.5 points per hour + random noise, capped at 100
scores = 45 + 5.5 * hours + rng.normal(0, 3, size=len(hours))
scores = np.clip(scores, 0, 100)

plt.scatter(hours, scores)
plt.xlabel("Hours studied")
plt.ylabel("Exam score")
plt.title("Study hours vs exam score")
plt.show()
