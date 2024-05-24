import matplotlib.pyplot as plt
import numpy as np


def simulate_bernoulli(n, p):
    #  Args:
    #    n: Number of samples.
    #    p: Success probability.

    return np.random.choice([0, 1], size=n, p=[1 - p, p])


def plot_sample_average(n, p):
    samples = simulate_bernoulli(n, p)
    sample_means = np.cumsum(samples) / np.arange(1, n + 1)

    plt.plot(sample_means)
    plt.xlabel("Iterations (k)")
    plt.ylabel("Sample Average")
    plt.title(f"Sample Average vs. Iterations (n={n}, p={p})")
    plt.grid(True)
    plt.show()


# Set parameters
n = 1000  # Number of coin tosses
p = 0.5  # Probability of success (fair coin)

plot_sample_average(n, p)
