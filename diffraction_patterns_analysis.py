# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:32:10 2015

@author: noam
"""

import os
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from scipy import optimize

os.chdir("/home/noam/studies/physics/lab_b/diffraction/")
from read_dscope_no_header import read_dscope_no_header
from angle_calibration import angle_error, intensity_error
from remove_saturated_data import remove_saturated_data
os.chdir("/home/noam/studies/physics/lab_b/diffraction/data_raw")
#%%
address = "8.txt"
w = 20.0 # um
wave_length = 632.8 * 10 ** (-3) # um
angle, intensity_v = read_dscope_no_header(address)

def sinc_square(theta, w_over_wave_length, scale, shift):
    return scale ** 2 * np.sinc((theta - shift) * w_over_wave_length) ** 2

d_theta = 0.05 # measured manually
w_over_wave_length_manual = 2 / d_theta
p0 = [w_over_wave_length_manual, 1, 0]
opt_params, opt_errors = sp.optimize.curve_fit(sinc_square, angle, intensity_v, p0=p0)
w_over_wave_length = opt_params[0]
scale = opt_params[1]
shift = opt_params[2]
w_over_wave_length_error = opt_errors[0,0]

plt.errorbar(angle, intensity_v, intensity_error, angle_error, "*", label="data")
plt.xlabel("angle[rad]")
plt.ylabel("intensity [AU]")
plt.title("intensity pattern - single slit")

#plt.plot(angle, sinc_square(angle, w_over_wave_length_manual, np.sqrt(0.44), 0.0089), label="mock")
plt.plot(angle, sinc_square(angle, w_over_wave_length, scale, shift), label=r"model:sinc$^2$($\frac{w}{\lambda}\theta$)")

plt.legend(loc='best')
#%%
IS_REMOVE_SATURATION = False
address = "14.txt"
wave_length = 632.8 * 10 ** (-3) # um
angle, intensity_v = read_dscope_no_header(address)
if IS_REMOVE_SATURATION:
    angle, intensity_v = remove_saturated_data(angle, intensity_v)

def sinc_cos_square(theta, w_over_wave_length, d_over_wave_length, scale, shift):
    return scale ** 2 * np.sinc((theta - shift) * w_over_wave_length) ** 2 * np.cos(np.pi * d_over_wave_length * theta) ** 2


d_theta_main_lobe = 0.03 # measured manually
d_theta_cos = 0.0025 # measured manually
w_over_wave_length_manual = 2 / d_theta_main_lobe
d_over_wave_length_manual = 1 / d_theta_cos
p0 = [w_over_wave_length_manual, d_over_wave_length_manual, 1, 0]
opt_params, opt_errors = sp.optimize.curve_fit(sinc_cos_square, angle, intensity_v, p0=p0)
w_over_wave_length = opt_params[0]
d_over_wave_length = opt_params[1]
scale = opt_params[2]
shift = opt_params[3]
w_over_wave_length_error = opt_errors[0,0]


plt.errorbar(angle, intensity_v, intensity_error, angle_error, "*", label="data")
plt.xlabel("angle[rad]")
plt.ylabel("intensity [AU]")
plt.title("intensity pattern - two slits")

#plt.plot(angle, sinc_cos_square(angle, w_over_wave_length_manual, d_over_wave_length_manual, 1, 0), label="mock")
plt.plot(angle, sinc_cos_square(angle, w_over_wave_length, d_over_wave_length, scale, shift), label=r"model:sinc$^2$($\frac{w}{\lambda}\theta$)$cos^2(\pi \frac{d}{\lambda}\theta)$")

plt.legend(loc='best')

#%%
address = "21.txt"
wave_length = 632.8 * 10 ** (-3) # um
angle, intensity_v = read_dscope_no_header(address)

def multiple_slits(theta, w_over_wave_length, d_over_wave_length, scale, shift):
    N = 4
    return scale ** 2 * np.sinc((theta - shift) * w_over_wave_length) ** 2 * np.sin(N * np.pi * d_over_wave_length * theta) ** 2 * np.sin(np.pi * d_over_wave_length * theta) ** (-2)

"""
d_theta_main_lobe = 0.03 # measured manually
d_theta_cos = 0.0025 # measured manually
w_over_wave_length_manual = 2 / d_theta_main_lobe
d_over_wave_length_manual = 1 / d_theta_cos
p0 = [w_over_wave_length_manual, d_over_wave_length_manual, 1, 0]
opt_params, opt_errors = sp.optimize.curve_fit(sinc_cos_square, angle, intensity_v, p0=p0)
w_over_wave_length = opt_params[0]
d_over_wave_length = opt_params[1]
scale = opt_params[2]
shift = opt_params[3]
w_over_wave_length_error = opt_errors[0,0]
"""

plt.errorbar(angle, intensity_v, intensity_error, angle_error, "*", label="data")
plt.xlabel("angle[rad]")
plt.ylabel("intensity [AU]")
plt.title("intensity pattern - two slits")

#plt.plot(angle, sinc_cos_square(angle, w_over_wave_length_manual, d_over_wave_length_manual, 1, 0), label="mock")
#plt.plot(angle, sinc_cos_square(angle, w_over_wave_length, d_over_wave_length, scale, shift), label=r"model:sinc$^2$($\frac{w}{\lambda}\theta$)$cos^2(\pi \frac{d}{\lambda}\theta)$")

plt.legend(loc='best')

#%%
address = "25.txt"
wave_length = 632.8 * 10 ** (-3) # um
angle, intensity_v = read_dscope_no_header(address)

def multiple_slits(theta, w_over_wave_length, d_over_wave_length, scale, shift):
    N = 4
    return scale ** 2 * np.sinc((theta - shift) * w_over_wave_length) ** 2 * np.sin(N * np.pi * d_over_wave_length * theta) ** 2 * np.sin(np.pi * d_over_wave_length * theta) ** (-2)

"""
d_theta_main_lobe = 0.03 # measured manually
d_theta_cos = 0.0025 # measured manually
w_over_wave_length_manual = 2 / d_theta_main_lobe
d_over_wave_length_manual = 1 / d_theta_cos
p0 = [w_over_wave_length_manual, d_over_wave_length_manual, 1, 0]
opt_params, opt_errors = sp.optimize.curve_fit(sinc_cos_square, angle, intensity_v, p0=p0)
w_over_wave_length = opt_params[0]
d_over_wave_length = opt_params[1]
scale = opt_params[2]
shift = opt_params[3]
w_over_wave_length_error = opt_errors[0,0]
"""

plt.errorbar(angle, intensity_v, intensity_error, angle_error, "*", label="data")
plt.xlabel("angle[rad]")
plt.ylabel("intensity [AU]")
plt.title("intensity pattern - two slits")

#plt.plot(angle, sinc_cos_square(angle, w_over_wave_length_manual, d_over_wave_length_manual, 1, 0), label="mock")
#plt.plot(angle, sinc_cos_square(angle, w_over_wave_length, d_over_wave_length, scale, shift), label=r"model:sinc$^2$($\frac{w}{\lambda}\theta$)$cos^2(\pi \frac{d}{\lambda}\theta)$")

plt.legend(loc='best')