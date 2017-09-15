#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/14'


import pandas as pd
from Func import shape_shower


data = pd.read_excel('../A/A题附件.xls', sheetname=0, header=None).values
# Get the data from attachment
shape_shower(data)
