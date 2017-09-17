#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Func import load_data, shape_shower


data = load_data('../A/A题附件.xls', sheetname=0, header=None)
shape_shower(data)
# 用于展示模具的图像
