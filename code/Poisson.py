from scipy.stats import poisson

# 1. Exactly 0 drops (PMF)
p_0 = poisson.pmf(0, 2)
print(f"Exactly 0 drops: {p_0:.4f}") 
# Output: 0.1353

# 2. At most 2 drops (CDF)
p_up_to_2 = poisson.cdf(2, 2)
print(f"At most 2 drops: {p_up_to_2:.4f}") 
# Output: 0.6767
