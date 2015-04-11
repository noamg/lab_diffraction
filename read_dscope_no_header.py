# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:36:57 2015

@author: noam
"""

import os
import numpy as np
import scipy as sp
from scipy import stats
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

from angle_calibration import angle_v_to_rad

def read_dscope_no_header(address, is_remove_zero_intensity=True):
    table = pd.read_csv(address, sep="\t")
    m = table.as_matrix(['Ch0 [V]', 'Ch1 [V]'])
    angle_v = m[:, 0]
    intensity_v = m[:, 1]
    angle = angle_v_to_rad(angle_v)
    
    if is_remove_zero_intensity:
        is_intensity_non_zero = intensity_v != 0
        intensity_v = intensity_v[is_intensity_non_zero]
        angle = angle[is_intensity_non_zero]
        
    return angle, intensity_v
        
#%%    

def visual_test_read_dscope_no_header():
    address = "8.txt"
    angle, intensity = read_dscope_no_header(address)
    plt.figure()
    plt.plot(angle)
    plt.figure()
    plt.plot(intensity)
    plt.figure()
    plt.plot(angle, intensity)
