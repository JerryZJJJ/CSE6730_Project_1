from prob_solver import *


def simulation(x, n, h_zero, mif2, mif3, ra_m, dc_m, ne_m):
    s_zero = storage_cal(h_zero)

    # simulations for A(no correlation between seasons)
    r_storage = np.zeros((x, n))  # results of x - seasonal storage(x * n)
    r_power = np.zeros((x, n))  # results of x - seasonal power(x * n)

    for i in range(n):
        storage = np.zeros((x, 1))  # storage of 8 seasons
        power = np.zeros((x, 1))  # power generation of 8 seasons

        for j in range(x):
            p = j % 4  # 0: J-F-K;  1: A-M-J;  2: J-A-S;  3: O-N-D

            # create inflow2 and inflow3 following normal distribution
            inflow_2 = np.random.normal(mif2[p][0], mif2[p][1])
            inflow_3 = np.random.normal(mif3[p][0], mif3[p][1])

            # find seasonal release, irrigation, evaporation
            ra = ra_m[p][0]
            dc = dc_m[p][0]
            ne = ne_m[p][0]

            if j == 0:
                prev_s = s_zero
            else:
                prev_s = storage[j - 1][0]

            eva = ne * area_cal(elevation_cal(prev_s))

            # water balance
            curr_s = prev_s + inflow_2 + inflow_3 - eva - ra - dc

            # update
            storage[j][0] = curr_s
            power[j][0] = energy_cal(ra, elevation_cal(curr_s))

        # save results
        r_storage[:, i] = storage[:, 0]
        r_power[:, i] = power[:, 0]

    # results of elevation
    r_elevation = elevation_cal(r_storage)

    return r_elevation, r_storage, r_power


if __name__ == "__main__":
    print()
