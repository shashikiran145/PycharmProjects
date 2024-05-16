import matplotlib.pyplot as plt
import numpy as np

def simulate_bernoulli(n, p):
  """Simulates a Bernoulli random variable with success probability p.

  Args:
    n: Number of samples.
    p: Success probability.

  Returns:
    A NumPy array of Bernoulli trials (0 for failure, 1 for success).
  """
  return np.random.choice([0, 1], size=n, p=[1 - p, p])

def plot_sample_average(n, p):
  """Plots the sample average vs. iterations for a Bernoulli trial.

  Args:
    n: Number of samples.
    p: Success probability.
  """
  samples = simulate_bernoulli(n, p)
  print(samples)
  sample_means = np.cumsum(samples) / np.arange(1, n + 1)

  plt.plot(sample_means)
  plt.xlabel("Iterations (k)")
  plt.ylabel("Sample Average")
  plt.title(f"Sample Average vs. Iterations (n={n}, p={p})")
  plt.grid(True)
  plt.show()

# Set parameters
n = 1000  # Number of coin tosses
p = 0.5   # Probability of success (fair coin)

plot_sample_average(n, p)