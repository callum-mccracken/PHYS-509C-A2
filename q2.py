from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import quad
from utils import binomial_pmf, uniform_pdf

N_TEST = 3330
N_CONTROL_2 = 157
N_CONTROL_1 = 3324

N_POS_IN_TEST = 50

N_FALSE_POS_IN_CONTROL_1 = 16
N_TRUE_POS_IN_CONTROL_1 = 0
N_FALSE_NEG_IN_CONTROL_1 = 0
N_TRUE_NEG_IN_CONTROL_1 = N_CONTROL_1 - N_FALSE_POS_IN_CONTROL_1


def prob_n_pos_control_1(n_pos, rate):
    """binomial, chances of getting n positives in control 1"""
    binomial_pmf(k=n_pos, n=N_CONTROL_1, p=rate)


N_TRUE_POS_IN_CONTROL_2 = 130
N_FALSE_POS_IN_CONTROL_2 = 0
N_FALSE_NEG_IN_CONTROL_2 = N_CONTROL_2 - N_TRUE_POS_IN_CONTROL_2
N_TRUE_NEG_IN_CONTROL_2 = 0


def prob_n_pos_control_2(n_pos, rate):
    """binomial, chances of getting n positives in control 1"""
    binomial_pmf(k=n_pos, n=N_CONTROL_2, p=rate)


# Calculate the Bayesian 95% central interval on the fraction
# of people in Santa Clara County who actually had antibodies for COVID-19,
# marginalizing over the false positive and false negative rates.
# Assume flat priors on all parameters.

real_antibody_rates = np.arange(0, 1, 0.001)

priors = uniform_pdf(real_antibody_rates, start=0, end=1)

def likelihood_func(real_ab_rate):
    """Single-variable function for integrating."""
    # prob of getting data given real_ab_rate
    n_pos_control_1 = N_CONTROL_1 * real_ab_rate
    prob_control_1 = prob_n_pos_control_1(n_pos, )
    prob_control_2 = prob_n_pos_control_2()
    return prob_control_1 * prob_control_2

def likelihood_func_single(m_val):
    """Single-variable function for integrating."""
    # product of individual likelihoods bc independent measurements (I assume)
    unif_probs = [uniform_pdf(x=obs, start=0, end=real_antibody_rates)
                  for obs in observations]
    return np.prod(unif_probs, axis=0)


likelihoods = likelihood_func_single(real_antibody_rates)
normalization = quad(likelihood_func, 0, 1)[0]
posteriors = likelihoods * priors / normalization

# Submit a plot of the posterior distribution for the true incidence rate
plt.plot(real_antibody_rates, posteriors)
