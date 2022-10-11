"""
Assume that the data follows an exponential plateau,
approaching some steady state value C.

Do a maximum likelihood fit for this level,
and determine the uncertainty on it.

Note that you have not been given the uncertainties on the measured
values -- instead, assume that all measurements have the same uncertainty
level, and fit for it as one of the parameters in your fit.

Submit your code, the functional form you fit,
and your result for the steady state value (with uncertainty).

What uncertainty value per data point did you get?

How much of that uncertainty can be attributed to the time binning
(measurements are only reported to the nearest minute)?
"""
from matplotlib import pyplot as plt
import numpy as np
from utils import gaussian_pdf
from scipy.optimize import minimize
from scipy.integrate import quad, dblquad

# x = minutes after start time
x_data = np.array([0, 6, 10, 14, 19, 24, 29, 33, 46, 54, 57])
# y = ppm
y_data = np.array([484, 501, 520, 535, 554, 565, 579, 593, 635, 651, 654])

def exponential_form(x, C=1, B=1, A=1):
    return C - B*np.exp(-A*x)

def prob_data(x, y, C, B, A, sigma):
    return gaussian_pdf(y, mu=exponential_form(x,C,B,A), sigma=np.abs(sigma))

def prob_data_no_B(x, y, C, A, sigma):
    return quad(lambda B: prob_data(x, y, C, B, A, sigma), a=-np.inf, b=np.inf)[0]

def prob_data_no_B_or_A(x, y, C, sigma):
    return quad(lambda A: prob_data_no_B(x, y, C, A, sigma), a=-np.inf, b=np.inf)[0]


def neg_log_likelihood(C, sigma):
    return -np.sum([prob_data_no_B_or_A(x, y, C, sigma) for x, y, in zip(x_data, y_data)])


# def nll_marginalized(C, sigma):
#     return dblquad(
#         lambda x,y: neg_log_likelihood(C, x, y, sigma),
#         a=0, b=-np.inf,
#         gfun=0, hfun=np.inf)[0]
# 
# Cs, sigmas = np.meshgrid(np.arange(0,1000,10), np.arange(0,10,0.1))
# nlls = np.zeros_like(Cs)
# for index, (c, sig) in enumerate(zip(Cs, sigmas)):
#     nlls[index] = nll_marginalized(c, sig)
# plt.plot(Cs, sigmas, c=nlls)
# plt.show()
def nll(params):
    """for integration purposes, with a single input variable"""
    return neg_log_likelihood(*params)


#print(prob_data(x_data[0], y_data[0], 924, 300, 0.016, 10))
#print(prob_data_no_B_or_A(x_data[0], y_data[0], 924, 10))

print(nll([924, 10]))
exit()

optimal_params = minimize(nll, x0=(924,10))
print(optimal_params)

C_0=770
B_0=300
A_0=0.016
sigma_0=0.1
plt.scatter(x_data, y_data)
plt.plot(x_data, exponential_form(x_data, C_0, B_0, A_0))
# plt.errorbar(x_data, y_data, yerr=[sigma_0]*len(x_data))
plt.savefig("q3.png")

# How much of that uncertainty can be attributed to the time binning
# (measurements are only reported to the nearest minute)?
