import numpy as np
import matplotlib.pyplot as plt


# Function to simulate Bernoulli trials and compute sample averages
def simulate_bernoulli_trials(n, p):
    trials = np.random.binomial(1, p, n)
    return np.cumsum(trials) / np.arange(1, n + 1)


# Part (a): Plotting the sample average vs iterations for a biased coin
def plot_sample_average_vs_iterations(n, p):
    sample_averages = simulate_bernoulli_trials(n, p)

    plt.figure(figsize=(10, 5))
    plt.plot(sample_averages, label=f'p={p}')
    plt.axhline(y=p, color='r', linestyle='--', label='True Mean')
    plt.xlabel('Iterations')
    plt.ylabel('Sample Average')
    plt.title('Sample Average vs Iterations')
    plt.legend()
    plt.show()


# Function to perform experiments and compute averages
def perform_experiments(n, m, p):
    averages_matrix = np.zeros((n, m))

    for k in range(1, n + 1):
        for j in range(m):
            sample = np.random.binomial(1, p, k)
            averages_matrix[k - 1, j] = np.mean(sample)

    return averages_matrix


# Part (b): Plotting average vs sample size with error bars
def plot_averages_with_error_bars(n, m, p):
    averages_matrix = perform_experiments(n, m, p)
    means = np.mean(averages_matrix, axis=1)
    std_devs = np.std(averages_matrix, axis=1)

    plt.figure(figsize=(10, 5))
    plt.errorbar(np.arange(1, n + 1), means, yerr=std_devs, fmt='o', label=f'p={p}')
    plt.axhline(y=p, color='r', linestyle='--', label='True Mean')
    plt.xlabel('Sample Size')
    plt.ylabel('Average')
    plt.title('Average vs Sample Size with Error Bars')
    plt.legend()
    plt.show()


# Main function to run the tests for p = 0.3 and p = 0.9
def main():
    n = 1000
    m = 10
    probabilities = [0.3, 0.9]

    for p in probabilities:
        print(f"Running simulation for p = {p}")
        # Part (a)
        plot_sample_average_vs_iterations(n, p)

        # Part (b)
        plot_averages_with_error_bars(n, m, p)


if __name__ == "__main__":
    main()
