"""
The percentage yield on an investment has a Gaussian distribution with mean
of 8% and standard deviation (SD) of 15%. (A yield of 8% would mean the amount
of money increases by a factor of 1.08 in a year.
A yield of -8% would mean multiplying by 0.92 instead.)

Suppose that you put $3000 into a retirement account investing in this item on
January 1st of every year, starting in 2018. What is the mean amount of money
you will have in the account on Dec 31, 2047?

Show a plot of the distribution of the amount of money on that date for
1000 trials of the "experiment". What is the SD?
Hand in your code or equivalent documentation.
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