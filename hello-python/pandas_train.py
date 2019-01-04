#!/usr/bin/python
# -*- coding=UTF-8 -*-

import pandas as pd

cols = ['Chinese', 'English', 'Math']

data = {'Chinese': [66, 95, 93, 90, 80, 80], 'English': [65, 85, 92, 88, 90, 90], 'Math': [None, 98, 96, 77, 90, 90]}
df = pd.DataFrame(data, index=['张飞', '关羽', '赵云', '黄忠', '典韦', '典韦'], columns=cols)

df = df.drop_duplicates()
df = df.filter(cols, axis=1)
df.rename(columns={'Chinese': '语文', 'English': '英语', 'Math': '数学'}, inplace=True)
print df


def total_score(df):
    df['总分'] = df['语文'] + df['英语'] + df['数学']
    return df


df = df.apply(total_score, axis=1)
# 或者可以用这个方法求和
# df['总分'] = df['语文'] + df['英语'] + df['数学']
# 按照总分排序，从高到低，此时有缺失值
df.sort_values(['总分'], ascending=[False], inplace=True)
# 打印显示成绩单信息，张飞有空值
print(df.isnull().sum())
print(df.describe())
print(df)

df['数学'].fillna(df['数学'].mean(), inplace=True)
# 再次求成绩的和并打印显示成绩单情况
df = df.apply(total_score, axis=1)
print(df.isnull().sum())
print(df.describe())
print(df)
