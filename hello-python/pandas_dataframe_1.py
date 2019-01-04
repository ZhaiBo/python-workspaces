#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
from pandas import DataFrame

# df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
# print df1.describe()
df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
df2 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2': range(5)})

df3 = pd.merge(df1, df2, on='name')
# 默认how=inner
# df4 = pd.merge(df1, df2, how='left')
# df4 = pd.merge(df1, df2, how='right')
df4 = pd.merge(df1, df2, how='outer')
print df4
