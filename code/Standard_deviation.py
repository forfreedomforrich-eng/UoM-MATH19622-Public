import numpy as np

data = [2, 4, 4, 4, 5, 5, 7, 9]

# 1. Population SD (divides by n) - RARELY USED
pop_sd = np.std(data) 

# 2. Sample SD (divides by n-1) - ENGINEERING STANDARD
# ddof = Delta Degrees of Freedom
sample_sd = np.std(data, ddof=1)

print(f"Sample Std Dev: {sample_sd:.2f}")
