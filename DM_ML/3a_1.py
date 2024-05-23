import numpy as np
import matplotlib.pyplot as plt

m = 1000
for n in [10, 25, 50, 100]:
    Z = []
    for _ in range(m):
        # Generate n i.i.d. samples from U(0, 1)
        X = np.random.uniform(0, 1, n)

        # Calculate sample mean (Sn)
        Sn = np.sum(X)

        # Calculate standardized value (Z)
        Z.append((Sn - n * 0.5) / (np.sqrt(1 / 12) * np.sqrt(n)))

def normal_pdf(x):
  return (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)

x = np.linspace(-3, 3, 100)  # Range for x-axis

plt.figure(figsize=(10, 6))
for i, n in enumerate([10, 25, 50, 100]):
  plt.subplot(2, 2, i + 1)
  plt.hist(Z[m * i: m * (i + 1)], bins=20, density=True, alpha=0.7, label='Sample Distribution')
  plt.plot(x, normal_pdf(x), label='Normal Distribution')
  plt.xlabel('Z')
  plt.ylabel('Probability Density')
  plt.title(f'Sample Size (n) = {n}')
  plt.legend()

plt.tight_layout()
plt.show()