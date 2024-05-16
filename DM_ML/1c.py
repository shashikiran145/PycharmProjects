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

def plot_sample_average(n):
  """Plots the sample average vs. iterations for a Bernoulli trial with varying p.

  Args:
    n: Number of samples.
  """
  biased_ps = [0.3, 0.9]  # List of success probabilities for biased coins
  for p in biased_ps:
    samples = simulate_bernoulli(n, p)
    sample_means = np.cumsum(samples) / np.arange(1, n + 1)

    plt.plot(sample_means, label=f"p={p}")  # Add label for each plot

  plt.xlabel("Iterations (k)")
  plt.ylabel("Sample Average")
  plt.title(f"Sample Average vs. Iterations (n={n})")
  plt.grid(True)
  plt.legend()  # Show legend for different probabilities
  plt.show()

def plot_experiment_averages(n, m):
  """Plots the average vs. sample size with error bars for multiple experiments with varying p.

  Args:
    n: Number of samples per experiment (k).
    m: Number of experiments.
  """
  biased_ps = [0.3, 0.9]  # List of success probabilities for biased coins
  for p in biased_ps:
    results = experiment(n, m, p)
    averages = np.mean(results, axis=0)
    stds = np.std(results, axis=0)

    plt.errorbar(np.arange(1, n + 1), averages, yerr=stds, fmt='o-', label=f"p={p}")

  plt.xlabel("Sample Size (k)")
  plt.ylabel("Average")
  plt.title(f"Averages vs. Sample Size with Error Bars (n={n}, m={m})")
  plt.grid(True)
  plt.legend()  # Show legend for different probabilities
  plt.show()

def experiment(n, m, p):
  """Performs m experiments of drawing k elements from a Bernoulli distribution.

  Args:
    n: Number of samples per experiment (k).
    m: Number of experiments.
    p: Success probability.

  Returns:
    A NumPy array of shape (m, n) containing averages for each experiment.
  """
  # ... (same as previous implementation)

# Set parameters
n = 1000
m = 10

# Call plotting functions
plot_sample_average(n)
plot_experiment_averages(n, m)