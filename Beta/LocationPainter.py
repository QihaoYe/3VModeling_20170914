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


data = pd.read_excel('../B/附件一：已结束项目任务数据.xls').values
# Get the data from attachment
locations = data[:, 1:3].astype(float)
# Get all the locations from data
isfinished = data[:, 4].astype(int)
# Get all the labels whether each is finished or not
locations_finished = locations[np.where(isfinished == 1)]
# Get all the locations that is finished
locations_unfinished = locations[np.where(isfinished == 0)]
# Get all the locations that is unfinished
plt.title('经纬度坐标以及完成情况示意图')
plt.xlabel('任务GPS纬度')
plt.ylabel('任务GPS经度')
plt.scatter(locations_finished[:, 0], locations_finished[:, 1], color='red', marker='o', label='被执行任务')
plt.scatter(locations_unfinished[:, 0], locations_unfinished[:, 1], color='blue', marker='o', label='未被执行任务')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()
