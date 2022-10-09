"""
Question 1 a)

Suppose the rate $R$ of visible galactic supernovae is unknown
but that supernovae follow a Poisson distribution.

In the past 10 centuries astronomers have observed 4 supernovae in our galaxy.

Assuming a uniform prior for the rate $R$,
use Bayes' theorem to calculate the probability distribution for $R$.

Now repeat the calculation, assuming this time that
the prior for R is uniform in log_10(R)
(i.e. it's equally probable that the true rate is between 0.02 and 0.2
as it is that it is between 0.2 and 2.0). Plot the resulting posterior
probability distribution for $R$ in both cases.
"""

from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import quad as integrate
from utils import uniform_pdf, poisson_pmf

OBSERVED_NUMBER = 4  # supernovae/millenium
UNIF_START = 0  # start of uniform distribution
UNIF_END = 10  # end of uniform distribution

def uniform_prior(rate):
    return 1

def likelihood_func(rate):
    """Single-variable function for integrating over rate for normalization"""
    return poisson_pmf(k=OBSERVED_NUMBER, rate=rate)

def normalization_integrand(prior, likelihood):
    """Single-variable function for integrating over rate for normalization"""
    return lambda x: prior(x) * likelihood(x)

# Assuming a uniform prior for the rate R,
# use Bayes' theorem to calculate the probability
# distribution for R.

rates = np.linspace(0.1,12,1000)
priors = uniform_prior(rates)
likelihoods = likelihood_func(rates)
normalization = integrate(normalization_integrand(
    uniform_prior, likelihood_func), 0, np.inf)[0]
posteriors = likelihoods * priors / normalization

plt.title("Q1. a)")
plt.xlabel("R")
plt.ylabel("posterior probability")
plt.plot(rates, posteriors, label="uniform R prior")

# Now do it with a uniform log_10(R) prior.
def uniform_log_prior(rate):
    # derived with P(x)dx = P(y)dy
    return 1 / (np.log(10)*rate)

priors2 = uniform_log_prior(rates)
likelihoods2 = likelihood_func(rates)
normalizations2 = integrate(normalization_integrand(
    uniform_log_prior, likelihood_func), 0, np.inf)[0]
posteriors2 = likelihoods2 * priors2 / normalizations2

plt.plot(rates, posteriors2, label="uniform log_10(R) prior")
plt.legend()
plt.savefig("q1_a.png")
