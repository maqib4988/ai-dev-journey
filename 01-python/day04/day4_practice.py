import pandas as pd
import numpy as np

# Creating a Series
prices = pd.Series([100, 250, 75, 300], name="price")
print(prices)

# Custom index (like naming each row instead of 0,1,2,3)
prices = pd.Series([100, 250, 75, 300], index=["apple", "laptop", "book", "phone"])
print(prices["laptop"])  

print(prices * 1.1)       # apply 10% price increase to all
print(prices[prices > 100])  # filter by condition

# Useful Series methods
print(prices.mean())
print(prices.sort_values())
print(prices.describe())  # count, mean, std, min, max, quartiles — all at once


# Creating a DataFrame from a dictionary
data = {
    "name": ["Aaqib", "Sara", "Bilal", "Hina"],
    "age": [28, 24, 31, 27],
    "city": ["Kohat", "Lahore", "Karachi", "Islamabad"],
    "salary": [85000, 72000, 95000, 68000]
}
df = pd.DataFrame(data)
print(df)

# Inspecting a DataFrame — do this FIRST on any new dataset, always
print(df.head())       # first 5 rows
print(df.tail(2))      # last 2 rows
print(df.shape)        # (4, 4) -> 4 rows, 4 columns
print(df.columns)      # column names
print(df.dtypes)       # data type of each column
print(df.info())       # combined summary: types, non-null counts, memory
print(df.describe())   # statistical summary of numeric columns

# Selecting columns
print(df["name"])              # single column -> returns a Series
print(df[["name", "salary"]])  # multiple columns -> returns a DataFrame

# Selecting rows
print(df.loc[0])           # row by label/index
print(df.iloc[0])          # row by position (same here since index is 0,1,2,3)
print(df.loc[0:2])         # rows 0 to 2 (inclusive)

# Adding a new column (vectorized, like Day 3 NumPy ops)
df["monthly_salary"] = df["salary"] / 12
print(df)

print(df.sort_values("salary", ascending=False))

# Single condition
high_earners = df[df["salary"] > 70000]
print(high_earners)

# Multiple conditions — use & (and) / | (or), and wrap each condition in parentheses
young_high_earners = df[(df["age"] < 30) & (df["salary"] > 70000)]
print(young_high_earners)

# Filtering by a list of values
target_cities = df[df["city"].isin(["Kohat", "Lahore"])]
print(target_cities)

# Filtering with string methods
starts_with_s = df[df["name"].str.startswith("S")]
print(starts_with_s)

data2 = {
    "department": ["Engineering", "Engineering", "Sales", "Sales", "Marketing"],
    "employee": ["Aaqib", "Sara", "Bilal", "Hina", "Omar"],
    "salary": [85000, 90000, 72000, 68000, 60000]
}
df2 = pd.DataFrame(data2)

# Group by department, get the average salary in each
avg_by_dept = df2.groupby("department")["salary"].mean()
print(avg_by_dept)

# Multiple aggregations at once
summary = df2.groupby("department")["salary"].agg(["mean", "min", "max", "count"])
print(summary)

# Group by and count rows per group
print(df2.groupby("department").size())

employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4],
    "name": ["Aaqib", "Sara", "Bilal", "Hina"],
    "dept_id": [10, 10, 20, 30]
})

departments = pd.DataFrame({
    "dept_id": [10, 20, 30],
    "dept_name": ["Engineering", "Sales", "Marketing"]
})

merged = pd.merge(employees, departments, on="dept_id")
print(merged)

# left join — keep all rows from 'employees' even if no match in 'departments'
merged_left = pd.merge(employees, departments, on="dept_id", how="left")
print(merged_left)