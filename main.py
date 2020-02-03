from mc_simulation import *
from plot_helper import *


def main():
    x = 8  # simulate x seasons
    n = 2000  # number of realizations
    h_zero = 175

    # matrix contains all parameters
    mif2 = [[2.025, 0.599, 0.5],
            [3.899, 1.630, 0],
            [40.71, 7.079, 0.6],
            [11.93, 3.534, 0]]
    mif3 = [[6.276, 0.99, 0.8],
            [5.775, 0.528, 0],
            [9.084, 0.611, 0.7],
            [10.041, 0.973, 0]]
    ra_m = [[10.25],
            [16.31],
            [18.64],
            [9.79]]
    dc_m = [[4.0],
            [2.22],
            [8.89],
            [8.89]]
    ne_m = [[0.501],
            [0.865],
            [0.839],
            [0.494]]

    elevation_a, storage_a, power_a = simulation(x, n, h_zero, mif2, mif3, ra_m, dc_m, ne_m)

    prob_mat = prob_cal(x, n, elevation_a)
    for i in range(np.size(prob_mat, 0)):
        print("probability of season " + str(i + 1) + " that over 178: " + "{:.4f}".format(prob_mat[i][1]) + '\n' +
              "probability of season " + str(i + 1) + " that lower than 168: " + "{:.4f}".format(prob_mat[i][0]) + '\n')

    plot_distribution(storage_a, 0)
    plot_distribution(power_a, 0)

    plot_statistic(elevation_a)
    plot_statistic(storage_a)
    plot_statistic(power_a)

    ite = 300
    elevation_steady = steady_state(ite, h_zero, mif2, mif3, ra_m, dc_m, ne_m)
    plot_steady_state(elevation_steady)


if __name__ == "__main__":
    main()
