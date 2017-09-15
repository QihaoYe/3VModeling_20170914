#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/15'


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('../A/A题附件.xls', sheetname=1, header=None).values
# Get the data from attachment
mid_line = np.average(data[255:257, :], axis=0)
plt.title('模具中线处对应接受射线能量强度-方向示意图')
plt.xlabel('方向')
plt.ylabel('中线处对应接受射线能量强度')
plt.plot(np.linspace(1, 180, 180), mid_line)
plt.show()
