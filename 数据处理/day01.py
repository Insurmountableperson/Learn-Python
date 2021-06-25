#  numpy 引入
import numpy as np

array = np.array([[1,2,3],
                  [2,3,4]])

print(array)                            #  输出矩阵
print('number of dimd:', array.ndim)    #  几维数组
print('shape:', array.shape)            #  行列
print('size:', array.size)              #  所有元素数

a = np.array([2, 23, 4], dtype=np.float32)  #  位数越小占用空间越小
print(a.dtype)

a = np.array([[2, 23, 4],
             [2, 32, 4]])
print(a)

a = np.zeros( (3,4) )   #  生成一个三行四列的全部为1的矩阵，中间为元组
print(a)
a = np.ones( (3,4) )    #  内容为 1
print(a)
a = np.empty((3,4))       #  几乎为 0 的矩阵
print(a)
a = np.arange(10,20,2)    #  起始值，终止值，步长
print(a)
a = np.arange(12).reshape((3,4))  #  重新定义一个3行4列的矩阵
print(a)


i1 = 1
i2 = 15
c = 4

a = np.linspace(i1,i2,c)#  .reshape((3,3))    ##  等差数列
# a = np.linspace(a, b, c)                     ## b-a/(c-1) = 每段长度

# print(a)
# b = (i2 - i1) / (c - 1)
# #  -----------------------
# c = ((i2-i1)/b)-1
print(i1,i2,c,'\n每段长度是：',b,'\n数组长度为：',len(a))


#  ---------------------------------
import pandas as pd
import matplotlib.pyplot as plt

test = pd.read_excel('D:/1.xlsx')
print(test)
