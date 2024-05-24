import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def simulate_clt(a, b, n, m):
  """
  Simulates the central limit theorem for a uniform distribution.

  Args:
      a (float): Lower bound of the uniform distribution.
      b (float): Upper bound of the uniform distribution.
      n (int): Number of independent random variables to sample.
      m (int): Number of iterations to perform.

  Returns:
      A NumPy array containing the standardized means (Z) for all iterations.
  """

  # Pre-calculate theoretical normal distribution parameters
  mu = (a + b) / 2  # Mean of the uniform distribution
  sigma = (b - a) / np.sqrt(12)  # Standard deviation of the uniform distribution
  theoretical_normal = norm.pdf(np.linspace(-5, 5, 1001), loc=0, scale=1)  # Theoretical normal distribution PDF

  # Initialize array to store standardized means
  Z = np.zeros(m)

  for i in range(m):
    # Simulate n independent random variables from the uniform distribution
    X = np.random.uniform(a, b, size=n)

    # Calculate sample mean (Sn)
    Sn = np.sum(X)

    # Calculate standardized mean (Z)
    Z[i] = (Sn - n * mu) / (sigma * np.sqrt(n))

  plt.figure(figsize=(10, 6))
  for i, n in enumerate([10, 25, 50, 100]):
    plt.subplot(2, 2, i + 1)
    plt.hist(Z[m * i: m * (i + 1)], bins=20, density=True, alpha=0.7, label='Sample Distribution')
    plt.plot(x, normal_pdf(x), label='Normal Distribution')
    plt.xlabel('Z')
    plt.ylabel('Probability Density')
    plt.title(f'Sample Size (n) = {n}')
    plt.legend()

# Define parameters
a = 0
b = 1
n_values = [10, 25, 50, 100]
m = 10000  # Number of iterations (increased for better visualization)

# Run simulations for different sample sizes
for n in n_values:
  Z = simulate_clt(a, b, n, m)
  plt.show()
