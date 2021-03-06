#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from Func import load_data


data = load_data('../A/A题附件.xls', sheetname=1, header=None)
mid_line = np.average(data[255:257, :], axis=0)
plt.title('模具中线处对应接受射线能量强度-方向示意图')
plt.xlabel('方向')
plt.ylabel('中线处对应接受射线能量强度')
plt.plot(np.linspace(1, 180, 180), mid_line)
plt.show()
# 做出模具中线处对应接受射线能量强度-方向示意图
