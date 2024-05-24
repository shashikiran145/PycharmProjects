import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def simulate_bernoulli(n, p):
    #  Simulates n Bernoulli trials with success probability p using vectorization.

    #  Args:
    #      n: Number of trials.
    #      p: Probability of success in each trial.

    return np.random.binomial(1, p, size=n)  # Vectorized generation


def calculate_normal_pdf(k, n, p):
    #  Calculates the probability density function (PDF) of the normal distribution.
    #  Args:
    #      k: Value for which to calculate the PDF.
    #      n: Number of trials in the Bernoulli simulation.
    #      p: Probability of success in each trial.

    mean = n * p
    std = np.sqrt(n * p * (1 - p))
    return norm.pdf(k, mean, std)


def analyze_results(n, p, m):
    #  Conducts the experiment m times, calculates statistics, and plots results.
    #  Args:
    #      n: Number of trials in each Bernoulli simulation.
    #      p: Probability of success in each trial.
    #      m: Number of iterations.

    # Pre-calculate theoretical normal distribution for all possible k values (0 to n)
    theoretical_normal = norm.pdf(np.arange(m * n + 1), n * p, np.sqrt(n * p * (1 - p)))

    # Conduct the experiment m times with vectorized operations
    successes = np.sum(simulate_bernoulli(m, p), axis=0)

    # Plot histograms
    plt.figure(figsize=(10, 6))
    plt.hist(successes, bins=20, edgecolor='black', alpha=0.7, label="Binomial (n=1000, p=0.3)")
    plt.plot(theoretical_normal, label="Normal Approximation")
    plt.xlabel("Number of Successes (k)")
    plt.ylabel("Frequency/Probability Density")
    plt.title(f"Binomial vs. Normal Distribution (n={n}, p={p}, m={m})")
    plt.legend()
    plt.tight_layout()
    plt.show()


# Define parameters
n = 1000
p = 0.3
m = 10 ** 5

# Run analysis
analyze_results(n, p, m)
