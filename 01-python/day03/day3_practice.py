import numpy as np

# simple method for adding arrays
a = [1, 2, 3]
b = [4, 5, 6]
result = [a[i] + b[i] for i in range(len(a))]
print(result)

#using numpy
a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))

# 2D array (like a matrix / table of rows and columns)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
print(matrix.shape)   # (2, 3) -> 2 rows, 3 columns
print(matrix.ndim)    # 2 -> number of dimensions
print(matrix.dtype)   # int64 (or similar) -> data type of elements

zeros = np.zeros((3, 3))        # 3x3 array of all zeros
ones = np.ones((2, 4))          # 2x4 array of all ones
identity = np.eye(3)            # 3x3 identity matrix (diagonal of 1s)
range_arr = np.arange(0, 10, 2) # [0, 2, 4, 6, 8] -> like Python's range()
linspace = np.linspace(0, 1, 5) # [0, 0.25, 0.5, 0.75, 1.0] -> 5 evenly spaced points

print(zeros)
print(ones)
print(identity)
print(range_arr)
print(linspace)

random_arr = np.random.rand(3, 3)         # random floats between 0 and 1
random_ints = np.random.randint(0, 10, 5) # 5 random ints between 0-9
print(random_arr)
print(random_ints)

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# Element-wise math — no loop required
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)

# Scalar operations (array + single number) applies to every element
print(a + 10)
print(a * 2) 

# Comparison operators return a boolean array
print(a > 2)

# Aggregate functions — reduce the whole array to one number
print(a.sum())     # 10
print(a.mean())    # 2.5
print(a.max())     # 4
print(a.min())     # 1
print(a.std())     # standard deviation

# For 2D arrays, you can aggregate along an axis
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.sum())            # 21 (sum of everything)
print(matrix.sum(axis=0))      # [5, 7, 9] -> sum down each column
print(matrix.sum(axis=1))      # [6, 15]   -> sum across each row

#indexing and slicing
a = np.array([10, 20, 30, 40, 50])
print(a[0])     # 10
print(a[-1])    # 50
print(a[1:4])   # [20, 30, 40]
print(a[:3])    # first 3 
print(a[::2])   # [10, 30, 50] -> every 2nd element

# 2D indexing: array[row, column]
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[0, 0])     # 1 -> row 0, col 0
print(matrix[1, 2])     # 6 -> row 1, col 2
print(matrix[0])        # [1, 2, 3] -> entire row 0
print(matrix[:, 0])     # [1, 4, 7] -> entire column 0
print(matrix[0:2, 1:3]) # [[2, 3], [5, 6]] -> sub-matrix (rows 0-1, cols 1-2) 0:2 → take rows with indexes 0 and 1,  1:3 → take columns with indexes 1 and 2

a = np.array([1, -2, 3, -4, 5, -6])
positive_only = a[a > 0]
print(positive_only)

# Modify values that match a condition
a[a < 0] = 0
print(a) 

# Simplest case: array + scalar 
a = np.array([1, 2, 3])
print(a + 5)

# Array + smaller array
matrix = np.array([[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]])
row_vector = np.array([10, 20, 30])

# row_vector gets "stretched" to match each row of matrix
print(matrix + row_vector)

# Practical example: normalize each column of a dataset
data = np.array([[1.0, 200.0], 
                  [2.0, 300.0], 
                  [3.0, 400.0]])
column_means = data.mean(axis=0)     # [2.0, 300.0]
column_stds = data.std(axis=0)       # std of each column

normalized = (data - column_means) / column_stds
print(normalized)
