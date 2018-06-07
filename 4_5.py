# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 19:05
# @Author  : Lxy
# @Site    :
# @File    : 4_5.py
# @Software: PyCharm

# 程序员面试经典
# 4.5树
# 检查是否为BST

'''
题目描述
请实现一个函数，检查一棵二叉树是否为二叉查找树。

给定树的根结点指针TreeNode* root，请返回一个bool，代表该树是否为二叉查找树。

<方法1>
      BST的中序遍历是升序数组

      首先我们想到的是二叉树中序遍历后的结果是有序的，根据这个结果，我们可以中序遍历二叉树，并把遍历结果存放在一个数组里面，

      然后判断这个数组大小是否是有序数组，如果是有序数组，则是二叉查找树，否则就不是。

       这个方法的时间复杂度是O(N)，但是空间复杂度比较高，需要浪费O（N）的存储空间。

<方法2>

      其实在<方法1>的基础上，我们可以在中序遍历的同时，比较大小，每次记录下上次遍历过的元素的值，

      如果当前元素的值大于上次遍历元素的值，则接着遍历，否则返回false，因为这个记录是一个址传递，所以需要用到引用形参进行传递。

     这个方法的时间复杂度与<方法1>的时间复杂度相同，只是空间复杂度只需要一个元素O(1)。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Checker:

    def checkBST(self, root):
        # write code here
        self.arr = []
        self.dfs(root)
        return self.arr == sorted(self.arr)

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.arr.append(root.val)
        self.dfs(root.right)
