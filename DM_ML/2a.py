import matplotlib.pyplot as plt
import numpy as np


def simulate_bernoulli(n, p):
    # Simulates n Bernoulli trials with success probability p.
    # Args:
    #      n: Number of trials.
    #      p: Probability of success in each trial.

    return np.random.binomial(1, p, n)


def compute_sample_average(data, m):
    # Calculates the sample average for each iteration (m).
    #  Args:
    #      data: A numpy array containing data for all iterations.
    #      m: Number of iterations.

    averages = np.zeros(m)
    for i in range(m):
        averages[i] = np.mean(data[:i + 1])
    return averages


def analyze_results(n, p, m):
    # Conducts the experiment m times, calculates statistics, and plots results.
    #  Args:
    #      n: Number of trials in each Bernoulli simulation.
    #      p: Probability of success in each trial.
    #      m: Number of iterations.

    # Initialize data structures
    successes = np.zeros(m)
    simulated_binomial = np.zeros(m)

    # Conduct the experiment m times
    for i in range(m):
        # Simulate Bernoulli trials and get number of successes
        coin_flips = simulate_bernoulli(n, p)
        successes[i] = np.sum(coin_flips)

        # Simulate binomial distribution and store value
        simulated_binomial[i] = np.random.binomial(n, p)

    # Calculate sample averages
    sample_averages = compute_sample_average(successes, m)

    # Plot histograms
    plt.figure(figsize=(10, 6))
    plt.subplot(121)
    plt.hist(successes, bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel("Number of Successes")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of Successes (Actual) (m = {m})")

    plt.subplot(122)
    plt.hist(simulated_binomial, bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel("Number of Successes")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of Simulated Binomial (m = {m})")
    plt.tight_layout()

    # Calculate mean squared error (MSE)
    mse = np.mean((successes - simulated_binomial) ** 2)

    # Print results
    print(f"Mean Sample Average: {np.mean(sample_averages)}")
    print(f"Mean Squared Error (MSE): {mse}")
    plt.show()


# Define parameters
n = 1000
p = 0.3
m_values = [10 ** 3, 10 ** 4, 10 ** 5]

# Run analysis for each value of m
for m in m_values:
    print(f"\nRunning analysis with m = {m}")
    analyze_results(n, p, m)
