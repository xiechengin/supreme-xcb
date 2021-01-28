'''
brief: 
Version: 
Autor: shuike
Date: 2021-01-11 16:47:16
LastEditors: shuike
LastEditTime: 2021-01-11 17:45:43
FilePath: /droneLanding/python/dataAnalyse.py
'''
from numpy import *
import matplotlib.pyplot as plt
import operator
from os import listdir

filename_x = "/Users/shuike/Desktop/work/svn/droneLanding/python/x.txt"
filename_z = "/Users/shuike/Desktop/work/svn/droneLanding/python/z.txt"
# fr = open(filename)
# numberofLines = len(fr.readlines())
# print("numberofLines",numberofLines)
# print("lines",fr.readlines())
# for line in fr.readlines():
#     print("line:",line.strip('\n').split(','))

import sys
result_x=[]
with open(filename_x,'r') as f:
	for line in f:
		result_x.append(float(line.strip('\n')))
print("result_x",result_x)


result_z=[]
with open(filename_z,'r') as f:
	for line in f:
		result_z.append(float(line.strip('\n')))
print("result_z",result_z)

plt.plot(result_z, result_x)
plt.show()


