#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/16'


import numpy as np
import matplotlib.pyplot as plt
from Func import load_data


data = load_data('../A/A题附件.xls', sheetname=1, header=None)
# Get the data from attachment
a = data[:, 60]
transformed=np.fft.fft(a)
# plt.plot(transformed)
shifted=np.fft.fftshift(transformed)
# plt.plot(shifted)
plt.plot(np.fft.ifft(shifted))
plt.show()
