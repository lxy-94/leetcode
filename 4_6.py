# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 19:45
# @Author  : Lxy
# @Site    :
# @File    : 4_6.py
# @Software: PyCharm

# 程序员面试经典
# 4.6树
# 寻找下一个结点

'''
题目描述

请设计一个算法，寻找二叉树中指定结点的下一个结点（即中序遍历的后继）。
给定树的根结点指针TreeNode* root和结点的值int p，请返回值为p的结点的后继结点的值。
保证结点的值大于等于零小于等于100000且没有重复值，若不存在后继返回-1。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Successor:
    def findSucc(self, root, p):
        # write code here
        self.arr = []
        self.dfs(root)
        n = self.arr.index(p)
        if self.arr[n + 1]:
            return self.arr[n + 1]
        else:
            return -1

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.arr.append(root.val)
        self.dfs(root.right)
