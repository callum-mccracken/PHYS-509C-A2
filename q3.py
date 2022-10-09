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
import numpy as np

data = {
    # time: ppm
    "13:20": 484,
    "13:26": 501,
    "13:30": 520,
    "13:34": 535,
    "13:39": 554,
    "13:44": 565,
    "13:49": 579,
    "13:53": 593,
    "14:06": 635,
    "14:14": 651,
    "14:17": 654}

def exponential_form(x, C=1, B=1, A=1):
    return C + B*np.exp(-A*x)

# do a max likelihood fit for C, with uncertainty


measurement_uncertainty = 10  # should fit for this

# How much of that uncertainty can be attributed to the time binning
# (measurements are only reported to the nearest minute)?
