#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/15'
__all__ = ['shape_shower']


import io
import sys
import numpy as np
import matplotlib.pyplot as plt


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# Change encoding into utf-8 for correctly printing


SIDE_LENGTH = 100
N = 256
row = np.linspace(0, SIDE_LENGTH, N).tolist()
rows = np.array([row] * N)
cols = rows.T


def shape_shower(data, title='模板', label='模具', legend=False, grid=True):
    """
    用于显示物品的几何信息
    其中data需为numpy.ndarray
    """
    x = rows[np.where(data == 1)]
    y = cols[np.where(data == 1)]
    plt.title(title + '几何信息示意图')
    plt.xlabel('正方形托盘边(mm)')
    plt.ylabel('正方形托盘边(mm)')
    plt.scatter(x, y, color='black', marker='o', label=label)
    plt.axis([0, 100, 0, 100])
    if legend:
        plt.legend(loc='upper right')
    if grid:
        plt.grid(True)
    plt.show()
