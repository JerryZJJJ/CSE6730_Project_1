import numpy as np


def statistics_cal(distribution):
    mean = np.mean(distribution, 1)
    maximum = np.max(distribution, 1)
    minimum = np.min(distribution, 1)
    std = np.std(distribution, 1)
    percentiles = np.percentile(distribution, [5, 25, 75, 95], 1)
    return mean, maximum, minimum, std, percentiles


# calculate prob of over 178 and lower than 168 for each season
def prob_cal(x, n, r_elevation):
    prob_mat = np.zeros((x, 2))
    over_178, lower_168 = 0, 0
    for p in range(x):
        over_178 = np.size((np.where(r_elevation[p, :] > 178)), 1)
        prob_mat[p, 1] = over_178 / n
        lower_168 = np.size((np.where(r_elevation[p, :] < 168)), 1)
        prob_mat[p, 0] = lower_168 / n
    return prob_mat


def steady_state(ite, h_zero, mif2, mif3, ra_m, dc_m, ne_m):
    storage = np.zeros((ite, 1))  # storage by seasons
    s_zero = storage_cal(h_zero)

    for i in range(ite):
        p = i % 4
        if2 = mif2[p][0]
        if3 = mif3[p][0]
        ra = ra_m[p][0]
        dc = dc_m[p][0]
        ne = ne_m[p][0]

        if i == 0:
            prev_s = s_zero
        else:
            prev_s = storage[i - 1, 0]
        eva = ne * area_cal(elevation_cal(prev_s))
        curr_s = prev_s + if2 + if3 - eva - ra - dc
        storage[i, 0] = curr_s
    seasonal_storage = np.reshape(storage, (4, -1), order="F")  # storage by seasons( in row)
    return elevation_cal(seasonal_storage)


# function that water elevation to storage curve
def elevation_cal(s):
    # para: storage, s_one
    # return: water elevation, h_one
    return 93.382075 * np.power(s, 0.1309)


def storage_cal(h):
    # para: water elevation, h_one
    # return: storage, s_one
    return np.power(h / 93.382075, 1 / 0.1309)


# area = ds/dh
def area_cal(h):
    # para: water elevation, h_one
    # return: area
    return 1 / 93.382075 / 0.1309 * np.power(h / 93.382075, 1 / 0.1309 - 1)


def energy_cal(r, h):
    # para: the reservoir release during the season
    # para: reservoir level at the beginning of the season
    # return: energy generation per season
    return 0.91 * 2.725 * r * (h - 110)


def elevation_prime_cal(s):
    return 12.224 * np.power(s, -0.8691)


def elevation_double_prime_cal(s):
    return -10.624 * np.power(s, -1.8691)


# 0.0818 * (h / 93.382075) ^ 6.6394
def area_prime_cal(h):
    return 0.0818 * 6.6394 / 93.382075 * np.power(h / 93.382075, 6.6394 - 1)


# 0.0058 * (h / 93.382075) ^ 5.6394
def area_double_prime_cal(h):
    return 0.0058 * 5.6394 / 93.382075 * np.power(h / 93.382075, 5.6394 - 1)


if __name__ == "__main__":
    print()