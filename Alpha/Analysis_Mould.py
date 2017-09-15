#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/15'


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('../A/A题附件.xls', sheetname=1, header=None).values
# Get the data from attachment
# mid_line = np.average(data[255:257, :], axis=0)
# plt.title('模具中线处对应接受射线能量强度-方向示意图')
# plt.xlabel('方向')
# plt.ylabel('中线处对应接受射线能量强度')
# plt.plot(np.linspace(1, 180, 180), mid_line)
# plt.show()
for i in range(512):
    plt.title('Receiver#%03d Value - Direction Diagram' % (i + 1))
    plt.xlabel('Direction')
    plt.ylabel('Receiver#%03d Value' % (i + 1))
    plt.plot(np.linspace(1, 180, 180), data[i, :])
    plt.axis([0, 180, 0, 150])
    plt.grid(True)
    plt.savefig('../receiver_direction/receiver%03d.png' % (i + 1))
    plt.close('all')
