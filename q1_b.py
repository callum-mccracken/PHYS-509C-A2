"""
For question 1. b)

Measurements are drawn from a uniform distribution on the interval (0, m).
The probability of getting a measurement outside of this range is zero.

The endpoint m is not well-known,
but a prior experiment yields a Gaussian prior of m = 3 +/- 1.

You take three measurements, getting values of 2.5, 3.1, and 2.9.

Use Bayes's theorem to calculate / plot the new probability distribution for m.
"""
from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import quad
from utils import gaussian_pdf, uniform_pdf

observations = [2.5, 3.1, 2.9]

# use Bayes' theorem to calculate the probability
# distribution for R.
m_step = 0.01
m_vals = np.arange(0.01, 500, m_step)
priors = gaussian_pdf(m_vals, mu=3, sigma=1)

def likelihood_func(m_val):
    """Single-variable function for integrating."""
    # product of individual likelihoods bc independent measurements (I assume)
    unif_probs = [uniform_pdf(x=obs, start=0, end=m_val)
                  for obs in observations]
    return gaussian_pdf(m_val, mu=3, sigma=1) * np.prod(unif_probs, axis=0)

def likelihood_func_single(m_val):
    """Single-variable function for integrating."""
    # product of individual likelihoods bc independent measurements (I assume)
    unif_probs = [uniform_pdf(x=obs, start=0, end=m_val)
                  for obs in observations]
    return np.prod(unif_probs, axis=0)



likelihood = likelihood_func_single(m_vals)
normalization = quad(likelihood_func, 0, np.inf)[0]
posterior = likelihood * priors / normalization

print(sum(posterior) * m_step)

plt.title("Q1. b)")
plt.xlabel("m")
plt.ylabel("posterior probability")
plt.plot(m_vals, posterior)
plt.xlim(0,20)
plt.savefig("q1_b.png")
