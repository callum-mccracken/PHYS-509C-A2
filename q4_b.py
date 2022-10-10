"""
Suppose now that the retirement account contains three classes of investments:
Canadian stocks, foreign stocks, and bonds. The yields on these three
investments each vary randomly but with some correlation. Here is the yield
information for each investment:

mu_C = 0.08
sigma_C = 0.15

mu_F = 0.08
sigma_F = 0.15

mu_B = 0.05
sigma_B = 0.07

rho_CF = 0.50
rho_CB = 0.20
rho_FB = 0.05

On January 1 of each year you put $1000 into each class of investment.
Show the distribution of the total amount of money in your account on
Dec 31, 2047. What are the mean and SD?

(Hint: generate a random yield drawn from a Gaussian distribution for the first
investment. Then generate a second Gaussian random number,
and form a linear combination of it and the first Gaussian number that will
have the desired SD and covariance. This is the yield of the second investment.
Then generate a third random number, and form a linear combination of all
three that will give the correct SD and covariance for the yield of this
combination with the other two yields.)
"""

import matplotlib.pyplot as plt
import numpy as np
import random

trials = np.array(range(1000))
years = np.array(range(2018, 2048))
values = np.zeros((len(trials), len(years)))

for i, trial in enumerate(trials):
    current_value_C = 1000
    current_value_F = 1000
    current_value_B = 1000
    for j, year in enumerate(years):
        # canadian stocks yield
        yld_C = random.gauss(mu=0.08, sigma=0.15)
        Y = random.gauss(mu=0, sigma=0.15)  # another Gaussian
        yld_F = Y - yld_C  # linear combo to get foreign stock yield
        yld_B = random.gauss(mu=0.05, sigma=0.174785583) + Y  # same w bonds
        current_value_C = 1000 + (1+yld_C) * current_value_C
        current_value_F = 1000 + (1+yld_F) * current_value_F
        current_value_B = 1000 + (1+yld_B) * current_value_B
        values[i, j] = current_value_C + current_value_F + current_value_B
    plt.scatter(years, values[i], alpha=0.05, c='b')
averages = np.mean(values, axis=0)
stds = np.std(values, axis=0)
plt.plot(years, averages, c='k')
plt.errorbar(years, averages, stds, c='k')
plt.savefig("q4_b.png")

print("Value Dec 31, 2047:", averages[-1])
print("Standard deviation:", stds[-1])
