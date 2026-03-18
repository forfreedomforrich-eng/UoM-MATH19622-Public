import numpy as np
from scipy import stats
# Our dataset (e.g., latency in ms)
data = [12, 15, 12, 200, 14]
# Calculate Measures
mean_val = np.mean(data) # Output: 50.6
median_val = np.median(data) # Output: 14.0
mode_val   = stats.mode(data, keepdims=True)
print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
# Access the first element [0] to get the value, not the count
print(f"Mode: {mode_val.mode[0]}")
