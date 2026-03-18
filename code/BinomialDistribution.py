from scipy.stats import binom

# binom.pmf(k, n, p)
p_8_heads = binom.pmf(8, 10, 0.5)

print(f"Probability of 8 heads: {p_8_heads:.4f}")
# Output: 0.0439
