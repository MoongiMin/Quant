import numpy as np

# ========== Create Arrays ==========
print("=== Create Arrays ===")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.zeros(5)
arr4 = np.ones((2, 3))
arr5 = np.arange(0, 10, 2)
arr6 = np.linspace(0, 1, 5)

print(f"1D array: {arr1}")
print(f"2D array:\n{arr2}")
print(f"Zeros array: {arr3}")
print(f"Ones array:\n{arr4}")
print(f"Range array: {arr5}")
print(f"Linspace array: {arr6}")

# ========== Array Shape and Size ==========
print("\n=== Array Shape and Size ===")
print(f"arr2 shape: {arr2.shape}")
print(f"arr2 size: {arr2.size}")
print(f"arr2 dtype: {arr2.dtype}")

# ========== Array Operations ==========
print("\n=== Array Operations ===")
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"a + b: {a + b}")
print(f"a * b: {a * b}")
print(f"a - b: {a - b}")
print(f"a / b: {a / b}")
print(f"a ** 2: {a ** 2}")

# ========== Mathematical Functions ==========
print("\n=== Mathematical Functions ===")
arr = np.array([1, 2, 3, 4, 5])
print(f"Sum: {np.sum(arr)}")
print(f"Mean: {np.mean(arr)}")
print(f"Std: {np.std(arr)}")
print(f"Min: {np.min(arr)}")
print(f"Max: {np.max(arr)}")

# ========== Useful for Quant (Stock prices) ==========
print("\n=== Quant Example: Stock Prices ===")
prices = np.array([100, 102, 101, 105, 103, 107, 106])
returns = np.diff(prices) / prices[:-1]  # Daily returns
print(f"Prices: {prices}")
print(f"Daily returns: {returns}")
print(f"Average return: {np.mean(returns):.4f}")
print(f"Volatility: {np.std(returns):.4f}")

# ========== Indexing and Slicing ==========
print("\n=== Indexing and Slicing ===")
arr = np.array([10, 20, 30, 40, 50])
print(f"First element: {arr[0]}")
print(f"Last element: {arr[-1]}")
print(f"First 3 elements: {arr[:3]}")
print(f"Elements from index 1 to 3: {arr[1:4]}")

# ========== Matrix Operations ==========
print("\n=== Matrix Operations ===")
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(f"Matrix 1:\n{m1}")
print(f"Matrix 2:\n{m2}")
print(f"Matrix product:\n{np.dot(m1, m2)}")



