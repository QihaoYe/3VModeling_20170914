#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__all__ = ['load_data', 'shape_shower', 'location_max_finder', 'differentiate', 'intensity_direction_shower', 'write_data', 'mix_pics']
import io
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 以防中文部分出现乱码


SIDE_LENGTH = 100
N = 256
row = np.linspace(0, SIDE_LENGTH, N).tolist()
rows = np.array([row] * N)
cols = rows.T


def load_data(address, sheetname=0, header=None):
    """
    从附件中得到数据
    """
    return pd.read_excel(address, sheetname=sheetname, header=header).values


def write_data(address, data, sheetname='page_1'):
    """
    将数据写入到Excel文件中
    """
    data_df = pd.DataFrame(data)
    writer = pd.ExcelWriter(address)
    data_df.to_excel(writer, sheetname, float_format='%.4f')
    writer.save()


def shape_shower(data, title='模板', label='模具', legend=False, grid=True):
    """
    用于显示物品的几何信息
    其中data要求为numpy.ndarray
    """
    x = rows[np.where(data > 0)]
    y = cols[np.where(data > 0)]
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


def get_boundary(value, grid=5, m='max'):
    """
    用于获得作图所需的上界和下界
    """
    if isinstance(value, int) is False and isinstance(value, float) is False:
        raise Exception('Value must be integer or float!')

    if m.lower() == 'max':
        value /= grid
        return np.ceil(value) * grid
    if m.lower() == 'min':
        value /= grid
        return np.floor(value) * grid


def intensity_direction_shower(data, direction=0, time=0, grid=True, save=False):
    """
    用于显示强度数据的图像
    """
    h, w = data.shape
    maximum = get_boundary(np.max(data), m='max')
    minimum = get_boundary(np.min(data), m='min')
    string = '' if time == 0 else ' Diff' if time == 1 else ' Diff of Order %d' % time
    plt.title('Direction#%03d%s Value - Receiver Diagram' % (direction + 1, string))
    plt.xlabel('Receiver')
    plt.ylabel('Direction#%03d%s Value' % (direction + 1, string))
    plt.plot(np.linspace(1, h, h), data[:, direction])
    plt.axis([0, h, minimum, maximum])
    plt.grid(grid)
    if save:
        plt.savefig('../direction_receiver_%d/direction%03d.png' % (time, direction + 1))
        plt.close('all')
    else:
        plt.show()


def location_max_finder(data):
    """
    用于寻找给定数据中的最大值的具体位置
    其中data要求为numpy.ndarray
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


def differentiate(data, n=1):
    """
    用于对数据进行求导
    其中data要求为numpy.ndarray
    """
    return np.diff(data, n=n, axis=0)


def mix_pics(pic1, pic2, address, weight=[1, 1]):
    """
    用来融合两张图片
    """
    import cv2
    img1 = cv2.imread(pic1)
    img2 = cv2.imread(pic2)
    weight1 = weight[0] / sum(weight)
    weight2 = weight[1] / sum(weight)
    img_mix = cv2.addWeighted(img1, weight1, img2, weight2, 0)
    cv2.imwrite(address, img_mix)
