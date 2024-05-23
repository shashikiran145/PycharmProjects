import numpy as np
import matplotlib.pyplot as plt


def simulate_bernoulli(n, p):
    #  Simulates n Bernoulli trials with success probability p.
    #  Args:
    #      n: Number of trials.
    #      p: Probability of success in each trial.

    return np.random.binomial(1, p, n)


def analyze_results(n, p_values, m):
    #  Conducts the experiment m times, calculates statistics, and plots results.
    #  Args:
    #      n: Number of trials in each Bernoulli simulation.
    #      p_values: List of probabilities for the binomial distribution.
    #      m: Number of iterations.

    for p in p_values:
        # Initialize data structures
        successes = np.zeros(m)
        simulated_poisson = np.zeros(m)

        # Conduct the experiment m times for each probability
        for i in range(m):
            # Simulate Bernoulli trials and get number of successes
            coin_flips = simulate_bernoulli(n, p)
            successes[i] = np.sum(coin_flips)

            # Simulate Poisson distribution with lambda (np)
            simulated_poisson[i] = np.random.poisson(n * p)

        # Plot histograms
        plt.figure(figsize=(10, 6))
        plt.hist(successes, bins=20, edgecolor='black', alpha=0.7, label=f"Binomial (n={n}, p={p})")
        plt.hist(simulated_poisson, bins=20, edgecolor='red', alpha=0.7, label=f"Poisson (lambda={n * p})")
        plt.xlabel("Number of Successes")
        plt.ylabel("Frequency")
        plt.title(f"Distribution of Successes (n={n}, m={m})")
        plt.legend()
        plt.tight_layout()

        # Calculate mean squared error (MSE) - optional for comparison
        mse = np.mean((successes - simulated_poisson)**2)
        print(f"Mean Squared Error (MSE - p={p}): {mse}")
        plt.show()


# Define parameters
n = 1000
p_values = [10 ** (-1), 10 ** (-2), 10 ** (-3)]
m = 10 ** 5

# Run analysis for each value of p
analyze_results(n, p_values, m)
