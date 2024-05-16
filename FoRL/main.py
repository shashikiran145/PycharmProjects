import math
import numpy as np
import matplotlib.pyplot as plt

z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def softmax():
    denominator = 0
    softmax_dist = []
    for j in range(len(z)):
        denominator = denominator + math.exp(z[j])
        print(denominator)
    for i in range(len(z)):
        numerator = math.exp(z[i])
        print(numerator)
        print((numerator/denominator))
        softmax_dist.append((numerator / denominator))
    print(softmax_dist)
    plt.plot(np.array(softmax_dist))
    plt.show()


softmax()

# a = [1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0]
# y = np.exp(a) / np.sum(np.exp(a))
# plt.plot(y)
# plt.show()








