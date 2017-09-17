#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from Func import load_data, write_data


mould = load_data('./extra/mould.xls')
mould[np.where(mould < 0.35)] = 0
write_data('./extra/mould.xlsx', mould, 'mould')
scale = 1 / (mould.sum() / len(mould[np.where(mould > 0)]))
write_data('./extra/mould.xlsx', mould * scale, 'mould')
q2 = load_data('./extra/problem2.xls')
q2[np.where(q2 < 0.1)] = 0
q3 = load_data('./extra/problem3.xls')
q3[np.where(q3 < 0.1)] = 0
write_data('./extra/problem2.xlsx', q2 * scale, 'q2')
write_data('./extra/problem3.xlsx', q3 * scale, 'q3')
# 讲得到的结果进行过滤和数值优化得到最终的结果并储存
