#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/16'


from Func import load_data, intensity_direction_shower, differentiate


LENGTH = 8
data = load_data('../A/A题附件.xls', sheetname=1, header=None)
# Get the data from attachment
intensity_direction_shower(differentiate(data, 2), 60)
