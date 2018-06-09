# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 17:49
# @Author  : Lxy
# @Site    : 
# @File    : 5_2.py
# @Software: PyCharm


# 程序员面试经典
# 5.2位运算
# 二进制插入

'''
题目描述
有一个介于0和1之间的实数，类型为double，返回它的二进制表示。如果该数字无法精确地用32位以内的二进制表示，返回“Error”。

给定一个double num，表示0到1的实数，请返回一个string，代表该数的二进制表示或者“Error”。

测试样例：
0.625
返回：0.101


对十进制小数乘2得到的整数部分和小数部分，

整数部分即是相应的二进制数码，

再用2乘小数部分(之前乘后得到新的小数部分)，又得到整数和小数部分。

如此不断重复,直到小数部分为0或达到精度要求为止.

第一次所得到为最高位,最后一次得到为最低位

如:

0.25的二进制

0.25*2=0.5   取整是0
0.5*2=1.0     取整是1

即0.25的二进制为 0.01 ( 第一次所得到为最高位,最后一次得到为最低位)

0.8125的二进制

0.8125*2=1.625  取整是1
0.625*2=1.25      取整是1
0.25*2=0.5          取整是0
0.5*2=1.0            取整是1

'''


class BinDecimal:
    def dec2bin(self, x):
        x -= int(x)
        bins = '0.'
        while x:
            x = x * 2
            bi = (1 if x >= 1. else 0)
            bins += str(bi)
            x -= int(x)
        return bins

    def printBin(self, num):
        x = self.dec2bin(num)
        if len(x) - 2 > 32:
            return 'Error'
        else:
            return x