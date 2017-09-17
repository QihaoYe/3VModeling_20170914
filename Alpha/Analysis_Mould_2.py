#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/15'


import numpy as np
import matplotlib.pyplot as plt
from Func import load_data


data = load_data('../A/A题附件.xls', sheetname=1, header=None)
for i in range(180):
    plt.title('Direction#%03d Value - Receiver Diagram' % (i + 1))
    plt.xlabel('Receiver')
    plt.ylabel('Direction#%03d Value' % (i + 1))
    plt.plot(np.linspace(1, 512, 512), data[:, i])
    plt.axis([0, 512, 0, 150])
    plt.grid(True)
    plt.savefig('../direction_receiver/direction%03d.png' % (i + 1))
    plt.close('all')
# 用于输出方向-接收器的图(对于每一个方向分别作图，共180张)
