import matplotlib.pyplot as plt
import numpy as np
import random

def simulate_bernoulli(n, p):
  """Simulates a Bernoulli random variable with success probability p.

  Args:
    n: Number of samples.
    p: Success probability.

  Returns:
    A NumPy array of Bernoulli trials (0 for failure, 1 for success).
  """
  print(p)
  return np.random.choice([0, 1], size=n, p=[1 - p, p])

def experiment(n, m, p):
  """Performs m experiments of drawing k elements from a Bernoulli distribution.

  Args:
    n: Number of samples per experiment (k).
    m: Number of experiments.
    p: Success probability.

  Returns:
    A NumPy array of shape (m, n) containing averages for each experiment.
  """
  results = np.zeros((m, n))
  for i in range(m):
    samples = simulate_bernoulli(n, p)
    results[i, :] = np.cumsum(samples) / np.arange(1, n + 1)
  return results

def plot_experiment_averages(n, m, p):
  """Plots the average vs. sample size with error bars for multiple experiments.

  Args:
    n: Number of samples per experiment (k).
    m: Number of experiments.
    p: Success probability.
  """
  results = experiment(n, m, p)
  averages = np.mean(results, axis=0)
  stds = np.std(results, axis=0)

  plt.errorbar(np.arange(1, n + 1), averages, yerr=stds, fmt='o-')
  plt.xlabel("Sample Size (k)")
  plt.ylabel("Average")
  plt.title(f"Averages vs. Sample Size with Error Bars (n={n}, m={m}, p={p})")
  plt.grid(True)
  plt.show()

# Set parameters
n = 10000  # Number of samples per experiment (k)
m = 10    # Number of experiments
p = 0.5   # Probability of success (fair coin)

plot_experiment_averages(n, m, p)