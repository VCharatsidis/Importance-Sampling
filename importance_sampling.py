import numpy as np
import seaborn as sns
from tqdm import trange
from scipy.stats import norm
from scipy.stats import uniform
import matplotlib.pyplot as plt



def importance_sampling():
    samples = 1000
    sims = 10000

    mu = 0
    sigma = 1

    low = -5
    high = 5

    expected_values = []
    for i in range(sims):

        X = np.random.normal(mu, sigma, samples)

        q = np.random.uniform(low, high, samples)

        p_x = norm(mu, sigma).pdf(q)
        q_x = uniform(low, high - low).pdf(q)

        weights = p_x / q_x

        # calculate X^2
        f_X = pow(X, 2)
        f_q = pow(q, 2)

        # calculate the expected value
        expected_values.append((weights.dot(f_q)) / samples)

    mean_expected_value = np.mean(expected_values)
    var_expected_value = np.var(expected_values)
    real_expected_value = sigma

    print("simulations "+str(sims))
    print("Importance Sampling of size "+str(samples))
    print("Simulated Expected value: "+str(mean_expected_value))
    print("Variance of the Expected value: "+str(var_expected_value))
    print("Actual Expected value: "+str(real_expected_value))

    # histogram generated by Importance Sampling
    n, bins, patches = plt.hist(expected_values, 50, density=1, facecolor='green', alpha=0.75)
    plt.ylabel('Frequency')
    plt.xlabel(r'Expected Value')
    plt.title("Importance Sampling")
    plt.grid(True)
    plt.show()

    # histogram from uniform samples weighted by the normal distribution
    n, bins, patches = plt.hist(weights*f_q, 50, density=1, facecolor='green', alpha=0.75)
    plt.ylabel('Number of Samples')
    plt.xlabel('X sampled from uniform distribution')
    plt.title("Histogram, Importance Sampling")
    plt.grid(True)
    plt.show()

    # histogram from normal samples
    n, bins, patches = plt.hist(f_X, 50, density=1, facecolor='blue', alpha=0.75)
    plt.ylabel('Number of Samples')
    plt.xlabel('sampled from normal distribution')
    plt.title("Histogram")
    plt.grid(True)
    plt.show()

    # weights
    plt.scatter(f_q, weights)
    plt.ylabel('weights')
    plt.xlabel(r'$X^2$')
    plt.title("Weights values")
    plt.grid(True)
    plt.show()

#importance_sampling()

def importance_sampling_2():
    samples = 1000
    sims = 10000

    mu = 0
    sigma = 1

    low = -1
    high = 1

    expected_values = []
    for i in range(sims):
        q = np.random.uniform(low, high, samples)

        # calculate weight
        p_x = (1 + np.cos(np.pi * q)) / 2
        q_x = uniform(low, high - low).pdf(q)
        weights = p_x / q_x

        # calculate X^2
        f_q = pow(q, 2)

        # calculate the expected value
        expected_values.append((weights.dot(f_q)) / samples)


    mean_expected_value = np.mean(expected_values)
    var_expected_value = np.var(expected_values)
    real_expected_value = sigma

    print("simulations " + str(sims))
    print("Importance Sampling of size " + str(samples))
    print("Simulated Expected value: " + str(mean_expected_value))
    print("Variance of the Expected value: " + str(var_expected_value))
    print("Actual Expected value: " + str(real_expected_value))

    # histogram generated by Importance Sampling
    n, bins, patches = plt.hist(expected_values, 50, density=1, facecolor='green', alpha=0.75)
    plt.ylabel('Frequency')
    plt.xlabel(r'Expected Value')
    plt.title("Importance Sampling")
    plt.grid(True)
    plt.show()

importance_sampling_2()