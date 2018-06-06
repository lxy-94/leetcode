# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 21:19
# @Author  : Lxy
# @Site    : 
# @File    : demo.py
# @Software: PyCharm

# 程序员面试经典
# 4.4树
# 输出单层节点
'''
题目描述

对于一棵二叉树，请设计一个算法，创建含有某一深度上所有结点的链表。
给定二叉树的根结点指针TreeNode* root，以及链表上结点的深度，请返回一个链表ListNode，
代表该深度上所有结点的值，请按树上从左往右的顺序链接，保证深度不超过树的高度，
树上结点的值为非负整数且不超过100000。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class TreeLevel:
    def getTreeLevel(self, root, dep):
        # write code here
        if dep < 0:
            return None
        if root == None:
            return None
        if dep == 1:
            return ListNode(root.val)

        first = []
        nextt = []
        first.append(root)
        h = 1

        while len(first) != 0:
            par = first.pop(0)
            if par.left:
                nextt.append(par.left)
            if par.right:
                nextt.append(par.right)
            if len(first) == 0:
                h += 1
                if h == dep:
                    break
                first = nextt
                nextt = []
        head = None
        pre = None
        for i in nextt:
            tNode = ListNode(i.val)
            if not head:
                head = tNode
                pre = head
            else:
                pre.next = tNode
                pre = pre.next
        return head