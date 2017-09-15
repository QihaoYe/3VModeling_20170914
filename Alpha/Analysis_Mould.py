#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/15'


import pandas as pd
import numpy as np


data = pd.read_excel('../A/A题附件.xls', sheetname=1, header=None).values
# Get the data from attachment
print(np.max(data))
