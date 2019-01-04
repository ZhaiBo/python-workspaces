#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np

x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)
# 加
print np.add(x1, x2)
# 减
print np.subtract(x1, x2)
# 乘
print np.multiply(x1, x2)
# 除
print np.divide(x1, x2)
# 求n次方
print np.power(x1, x2)
# 取余数
print np.remainder(x1, x2)

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print np.amin(a)
print np.amin(a, 0)
print np.amin(a, 1)
print np.amax(a)
print np.amax(a, 0)
print np.amax(a, 1)

'''
a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
b[1,1] = 10
print a.shape
print b.shape
print a.dtype
print b
'''

# 统计最大值最小值之差
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print np.ptp(b)
print np.ptp(b, 0)
print np.ptp(b, 1)

# 统计数组的百分位数 0求最小值 50求平均值 100求最大值
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print np.percentile(c, 100)
print np.percentile(c, 50, axis=0)
print np.percentile(c, 50, axis=1)

# 统计数组的中位数median()、平均数mean()
d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 求中位数
print np.median(d)
print np.median(d, axis=0)
print np.median(d, axis=1)
# 求平均数
print np.mean(d)
print np.mean(d, axis=0)
print np.mean(d, axis=1)

# 统计数组的加权平均值
e = np.array([1, 2, 3, 4])
wts = np.array([1, 2, 3, 4])
print np.average(e)
# np.average(a,weights=wts)=(1*1+2*2+3*3+4*4)/(1+2+3+4)=3.0
print np.average(e, weights=wts)

# 统计数组的标准差、方差
# 方差的计算是指每个数值与平均值之差的平方求和的平均值
# 标准差是方差的算术平方根
f = np.array([1, 2, 3, 4])
print np.std(f)
print np.var(f)

# NumPy 排序 sort(a, axis=-1, kind='quicksort’, order=None)
g = np.array([[4, 3, 2], [2, 4, 1]])
print np.sort(g)
print np.sort(g, axis=None)
print np.sort(g, axis=0)
print np.sort(g, axis=1)
