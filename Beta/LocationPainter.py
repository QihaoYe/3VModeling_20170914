#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/14'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
