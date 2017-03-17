# _*_ coding: utf-8 _*_

# @Time     :2017.3.13 下午 9:48
# @Author   :ZuMing Shen
# File      :2.Add Two Numbers.py
# software  :PyCharm


# class ListNode(object):           #Definition for singly-linked list
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def addTwoNumbers(self, l1, l2):
    """
    :param self:
    :param l1: ListNode
    :param l2: ListNode
    :return: ListNode
    """
    if l1 == None:
        return l2
    if l2 == None:
        return l1


def listTolong(self, l1, l2):
    num1, num2 = 0, 0
    temp1, temp2 = 1, 1
    for i in range(len(l1)):
        num1 += l1[i]
        temp1 *= 10
    for j in range(len(l2)):
        num2 += l2[j]
        temp2 *= 10
    num3 = num1 + num2
    lists = map(int, str([num3][0]))
    return lists

