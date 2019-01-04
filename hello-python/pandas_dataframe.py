#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
from pandas import DataFrame

# 读写excel
# score = DataFrame(pd.read_excel('data.xls', 1))
# score.to_excel('data1.xlsx')
# print score

data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])

print df1
print df2

# df2 = df2.drop(columns=['Chinese'])
# df2 = df2.drop(index=['ZhangFei'])

# df2.rename(columns={'Chinese': 'YuWen', 'English': 'Yingyu'}, inplace = True)
# df = df.drop_duplicates() # 去除重复行

# 更改数据格式
# df2['Chinese'].astype('str')
# df2['Chinese'].astype(np.int64)

# 删除左右两边空格
# df2['Chinese'] = df2['Chinese'].map(str.strip)
# 删除左边空格
# df2['Chinese'] = df2['Chinese'].map(str.lstrip)
# 删除右边空格
# df2['Chinese'] = df2['Chinese'].map(str.rstrip)

# 删除特定字符
# df2['Chinese'] = df2['Chinese'].str.strip('$')

# 全部大写
# df2.columns = df2.columns.str.upper()
# 全部小写
# df2.columns = df2.columns.str.lower()
# 首字母大写
# df2.columns = df2.columns.str.title()

# 查找空值
# df2.isnull() df2.isnull().any()
