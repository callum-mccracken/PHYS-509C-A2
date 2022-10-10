"""
Now suppose we add a procedure called ``rebalancing''.
On January 1 of each year we contribute a total of \$3000 to the account,
but at the same time we redistribute the total amount of money in the account
evenly between the three investments.

How does this change the total amount on Dec 31, 2047?
Show a plot of the distribution, and report the mean and SD as well.
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
        yld_C = random.gauss(mu=0.08, sigma=0.15)
        Y = random.gauss(mu=0, sigma=0.15)
        yld_F = Y - yld_C
        yld_B = random.gauss(mu=0.05, sigma=0.174785583) + Y
        current_value_C = (1+yld_C) * current_value_C
        current_value_F = (1+yld_F) * current_value_F
        current_value_B = (1+yld_B) * current_value_B
        total = current_value_C + current_value_B + current_value_F + 3000
        current_value_C = total / 3
        current_value_F = total / 3
        current_value_B = total / 3
        values[i, j] = total
    plt.scatter(years, values[i], alpha=0.05, c='b')
averages = np.mean(values, axis=0)
stds = np.std(values, axis=0)
plt.plot(years, averages, c='k')
plt.errorbar(years, averages, stds, c='k')
plt.savefig("q4_c.png")

print("Value Dec 31, 2047:", averages[-1])
print("Standard deviation:", stds[-1])
