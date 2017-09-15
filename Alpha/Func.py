#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/15'
__all__ = ['shape_shower', 'location_max_finder']


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


def location_max_finder(data):
    """
    用于寻找给定数据中的最大值的具体位置
    其中data需为numpy.ndarray
    """
    h, w = data.shape
    value = np.max(data)
    row = np.linspace(0, w - 1, w).tolist()
    rows = np.array([row] * h)
    col = np.linspace(0, h - 1, h).tolist()
    cols = np.array([col] * w).T
    x = rows[np.where(data == value)]
    y = cols[np.where(data == value)]
    print([int(y[0]), int(x[0])], value)
