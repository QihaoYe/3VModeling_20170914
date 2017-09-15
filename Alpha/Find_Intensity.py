#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/15'


import pandas as pd
from Func import location_max_finder


data = pd.read_excel('../A/A题附件.xls', sheetname=1, header=None).values


location_max_finder(data)
# print(data[:100, 150].reshape((100,1)))
location_max_finder(data[:100, 150].reshape((100,1)))
