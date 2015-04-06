# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:04:52 2015

@author: noam
"""

import glob
import os.path

data_dir = "./data"
new_data_dir = "./data_raw"
LINE_OF_TITLES = 5

for address in glob.glob(os.path.join(data_dir, "*.txt")):
    file_read = file(address, "rb")
    file_write = file(os.path.join(new_data_dir, os.path.basename(address)), "wb")
    lines = file_read.readlines()
    lines_out = lines[LINE_OF_TITLES:]
    file_write.writelines(lines_out)
    file_read.close()
    file_write.close()