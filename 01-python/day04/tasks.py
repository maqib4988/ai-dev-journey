from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(BASE_DIR / "train.csv")

print(df.shape)
print(df.info())
print(df.head())

# Find missing values
print(df.isnull().sum())
# Clean: fill missing Age with the median age
df["Age"] = df["Age"].fillna(df["Age"].median())

# Drop a column that's mostly missing or not useful (e.g. Cabin)
df = df.drop(columns=["Cabin"])

# Summary stats
print(df.describe())

# GroupBy: survival rate by passenger class
survival_by_class = df.groupby("Pclass")["Survived"].mean()
print(survival_by_class)

# GroupBy: survival rate by sex
survival_by_sex = df.groupby("Sex")["Survived"].mean()
print(survival_by_sex)

# Filter: female passengers in 1st class who survived
example = df[(df["Sex"] == "female") & (df["Pclass"] == 1) & (df["Survived"] == 1)]
print(example.shape)