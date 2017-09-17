#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Team19029042'
__data__ = '2017/9/14'


from Func import load_data, shape_shower


data = load_data('../A/A题附件.xls', sheetname=0, header=None)
shape_shower(data)
