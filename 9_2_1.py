# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 21:48
# @Author  : Lxy
# @Site    : 
# @File    : 9_2_1.py
# @Software: PyCharm

# 程序员面试经典
# 9.2_1递归和动态规划
# 机器人走方格I

# 题目描述
# 有一个XxY的网格，一个机器人只能走格点且只能向右或向下走，要从左上角走到右下角。请设计一个算法，计算机器人有多少种走法。
#
# 给定两个正整数int x,int y，请返回机器人的走法数目。保证x＋y小于等于12。

#   因为给出x+y<=12，所以不需要考虑递归超时问题
#   基本递归问题
class Robot:
    def countWays(self, x, y):
        # write code here
        if x == 0 or y == 0:
            return 0
        if x == 1 or y == 1:
            return 1
        return self.countWays(x-1,y)+self.countWays(x,y-1)