#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/17'


import numpy as np
from Func import write_data


data = np.zeros((512, 512))
data[143:399, 151] = 1
data[143:399, 406] = 1
data[143, 151:407] = 1
data[398, 151:407] = 1
write_data('./extra/Frame.xlsx', data, sheetname='Frame')
# 用于构造Frame并存在Excel表格中
