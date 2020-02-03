import matplotlib.pyplot as plt
from prob_solver import *


def plot_distribution(distribution, season):
    plt.hist(distribution[season, :])
    plt.show()


def plot_statistic(distribution):
    season = np.arange(0, 8, 1)
    mean, maximum, minimum, std, percentiles = statistics_cal(distribution)
    plt.plot(season, mean)
    plt.plot(season, maximum)
    plt.plot(season, minimum)
    for i in range(len(percentiles)):
        plt.plot(season, percentiles[i])
    plt.show()


def plot_steady_state(distribution):
    x = np.arange(0, np.size(distribution, 1), 1)
    for i in range(np.size(distribution, 0)):
        plt.plot(x, distribution[i, :])
    plt.show()


if __name__ == "__main__":
    print()