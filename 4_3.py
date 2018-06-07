# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 21:01
# @Author  : Lxy
# @Site    :
# @File    : 4_3.py
# @Software: PyCharm

# 程序员面试经典
# 4.3树
# 高度最小的BST
'''
题目描述

对于一个元素各不相同且按升序排列的有序序列，
请编写一个算法，创建一棵高度最小的二叉查找树。
给定一个有序序列int[] vals,请返回创建的二叉查找树的高度。
'''


class MinimalBST:
    left = right = 0

    def buildMinimalBST(self, vals):
        return self.createBST(vals, 0, len(vals) - 1)

    def createBST(self, vals, start, end):
        if start > end:
            return 0
        mid = start + (end - start) // 2
        self.left = self.createBST(vals, start, mid - 1) + 1
        self.right = self.createBST(vals, mid + 1, end) + 1
        return max(self.left, self.right)
