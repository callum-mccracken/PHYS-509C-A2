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
    current_value = 3000
    for j, year in enumerate(years):
        yld = random.gauss(mu=0.08, sigma=0.15)  # yield for this year
        current_value = 3000 + (1+yld) * current_value
        values[i, j] = current_value
    plt.scatter(years, values[i], alpha=0.05, c='b')
averages = np.mean(values, axis=0)
stds = np.std(values, axis=0)
plt.plot(years, averages, c='k')
plt.errorbar(years, averages, stds, c='k')
plt.savefig("q4_a.png")

print("Value Dec 31, 2047:", averages[-1])
print("Standard deviation:", stds[-1])
