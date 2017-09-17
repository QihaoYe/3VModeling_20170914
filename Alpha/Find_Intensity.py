#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/15'


from Func import load_data, location_max_finder


data = load_data('../A/A题附件.xls', sheetname=1, header=None)
location_max_finder(data)
location_max_finder(data[:100, 150].reshape((100, 1)))
location_max_finder(data[:, 60].reshape((512, 1)))
# 用于寻找出部分极值点在图表中的位置
