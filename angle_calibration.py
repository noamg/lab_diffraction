# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:23:31 2015

@author: noam
"""
import os
import numpy as np
import scipy as sp
from scipy import stats
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

IS_SHOW_GRAPHS = False

ANGLE_MAX = 10
ANGLE_MIN = -10

data = "./data_raw"
os.chdir(data)

plt.close("all")

# calibration
address = "7.txt"
table = pd.read_csv(address, sep="\t")
m = table.as_matrix(['Ch0 [V]', 'Ch1 [V]'])
angle_v = m[:, 0]
intensity_v = m[:, 1]
time = table['Ch0 [S]'].as_matrix()
if IS_SHOW_GRAPHS:
    plt.figure()
    plt.plot(angle_v, intensity_v, "*")
    plt.title("angle, intensity" + address)
    #print angle_v[intensity_v > 4].mean()
    plt.figure()
    plt.plot(time, angle_v, "*")
    plt.xlabel("time")
    plt.ylabel("angle_v")
    plt.title(address)

ind = time < 38
time = time[ind]
angle_v = angle_v[ind]
angle_deg = time / time.max() * (ANGLE_MAX - ANGLE_MIN) + ANGLE_MIN
angle_rad = angle_deg / 180 * np.pi

if IS_SHOW_GRAPHS:
    plt.figure()
    plt.plot(angle_v, angle_rad, ".", label="data")
    plt.xlabel("angle [volt]")
    plt.ylabel("angle [rad]")

slope, intercept, _, _, err = sp.stats.linregress(angle_v, angle_rad)
def angle_v_to_rad(a):
    return a * slope + intercept

if IS_SHOW_GRAPHS:
    plt.plot(angle_v, angle_v_to_rad(angle_v), linewidth=2, label="linear_fit")
    plt.legend(loc='best')
    plt.title("calibration of angle measurement")
    
angle_error_v = 0.00245 / 2 # measured manually using histogram
# plt.hist(np.diff(angle_v), bins=500)
angle_error = angle_error_v * slope
intensity_error = 0.022 - 0.020 # manually measured










