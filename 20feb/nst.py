# ----------------------------------------
# NumPy Speed Test
# ----------------------------------------

import time
import numpy as np

# Number of elements
N = 1_000_000

print("=== NumPy vs Python List Speed Test ===\n")

# ---------------------------
# Python List Test
# ---------------------------
start_time = time.time()

python_list = [i for i in range(N)]
squared_list = [x * x for x in python_list]

end_time = time.time()
python_time = end_time - start_time

print(f"Python List Time: {python_time:.4f} seconds")


# ---------------------------
# NumPy Array Test
# ---------------------------
start_time = time.time()

numpy_array = np.arange(N)
squared_array = numpy_array * numpy_array

end_time = time.time()
numpy_time = end_time - start_time

print(f"NumPy Array Time: {numpy_time:.4f} seconds")


# ---------------------------
# Performance Comparison
# ---------------------------
print("\n=== Comparison Result ===")

if numpy_time < python_time:
    print(f"NumPy is faster by {python_time - numpy_time:.4f} seconds.")
else:
    print(f"Python List is faster by {numpy_time - python_time:.4f} seconds.")