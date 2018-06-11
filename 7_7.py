# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 21:08
# @Author  : Lxy
# @Site    : 
# @File    : 7_7.py
# @Software: PyCharm

# 程序员面试经典
# 7.7数学基础
# 第7个数


# 题目描述
# 有一些数的素因子只有3、5、7，请设计一个算法，找出其中的第k个数。
#
# 给定一个数int k，请返回第k个数。保证k小于等于100。


#   暴力解法，每个数都需要判断，时间复杂度不高
class KthNumber:
    def isnum(self,number):
        if number%3 == 0:
            number /=3
        if number%5 == 0:
            number /=5
        if number%7 == 0:
            number /=7
        return number == 1
    def findKth(self, k):
        # write code here
        num = []
        i = 3
        while len(num) <k:
            if self.isnum(i):
                num.append(i)
            i += 1
        return num[k-1]


#   按顺序的第k个数只能是3、5、7的倍数，可以初始三个指针并不断更新判断即可。
class KthNumber_2:
    def findKth(self, k):
        if k==0:
            return 0
        index3 = index5 = index7 = 0
        n = 1
        su = [1]
        while n < k+1:
            Min = min(su[index3]*3, su[index5]*5, su[index7]*7)
            su.append(Min)
            while su[index3]*3 <= su[n]:
                index3 += 1
            while su[index5]*5 <= su[n]:
                index5 += 1
            while su[index7]*7 <= su[n]:
                index7 += 1
            n += 1
        return su[n-1]
