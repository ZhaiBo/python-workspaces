#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pandas import Series

x1 = Series([1, 2, 3, 4])
print x1

x2 = Series([5, 6, 7, 8], index=['a', 'b', 'c', 'd'])
print x2

print sorted(x1, reverse=True)
