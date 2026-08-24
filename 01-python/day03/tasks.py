import numpy as np

# an array of 20 random integers between 1-100. Print its mean, max, min, and standard deviation.

numbers = np.random.randint(1, 101, size=20)

print("Array:", numbers)
print("Mean:", numbers.mean())
print("Maximum:", numbers.max())
print("Minimum:", numbers.min())
print("Standard deviation:", numbers.std())

# a 4x4 matrix of random integers. Print the sum of each row and the sum of each column separately.

matrix = np.random.randint(1, 101, size=(4, 4))

print("Matrix:")
print(matrix)

print("\nSum of each row:")
print(matrix.sum(axis=1))

print("\nSum of each column:")
print(matrix.sum(axis=0))

# an array of 15 random integers between -50 and 50. Replace all negative values with 0, then print the result.

numbers = np.random.randint(-50, 51, size=15)

numbers[numbers < 0] = 0

print(numbers)

# a 1D array with numbers 1 to 12 using np.arange(1, 13), then reshape it into a 3x4 matrix using .reshape(3, 4). Print both the original and reshaped versions.

numbers = np.arange(1, 13)
matrix = numbers.reshape(3, 4)

print("Original 1D array:")
print(numbers)

print("\nReshaped 3x4 matrix:")
print(matrix)

# a 5x3 array of random values between 0-100 (imagine 5 samples, 3 features — like height, weight, age). Normalize it so each column has mean 0 and standard deviation 1.

data = np.random.randint(0, 101, size=(5, 3))

column_means = data.mean(axis=0)
column_stds = data.std(axis=0)

normalized_data = (data - column_means) / column_stds

print("Original data:")
print(data)

print("\nNormalized data:")
print(normalized_data)

print("\nMeans per column:", normalized_data.mean(axis=0))
print("Standard deviations per column:", normalized_data.std(axis=0))