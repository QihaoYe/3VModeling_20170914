#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/14'


import io
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# Change encoding into utf-8 for correctly printing


data = pd.read_excel('../A/A题附件.xls', sheetname=0, header=None).values
# Get the data from attachment
row = np.linspace(0, 100, 256).tolist()
rows = np.array([row] * 256)
cols = rows.T
x = rows[np.where(data == 1)]
y = cols[np.where(data == 1)]
plt.title('模板几何信息示意图')
plt.xlabel('正方形托盘边(mm)')
plt.ylabel('正方形托盘边(mm)')
plt.scatter(x, y, color='black', marker='.', label='模具')
plt.axis([0, 100, 0, 100])
plt.legend(loc='upper right')
plt.grid(True)
plt.show()
