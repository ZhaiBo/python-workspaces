#!/usr/bin/python
# -*- coding=UTF-8 -*-

import pandas as pd
from pandas import DataFrame
from pandasql import sqldf, load_meat, load_births

df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data': range(5)})
# pysqldf = lambda sql: sqldf(sql, globals())
# result = "select * from df1 where name ='ZhangFei'"
# print pysqldf(result)


#  lambda argument_list: expression
pysqldf = lambda sql: sqldf(sql, globals())

sql = "select * from df1 where name ='GuanYu'"

print pysqldf(sql)
