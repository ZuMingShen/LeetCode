# _*_ coding: utf-8 _*_

# @Time     :2017.3.20 下午 10:40
# @Author   :ZuMing Shen
# File      :7.Reverse Integer.py
# software  :PyCharm


class Solution(object):

    def reverse(self, x):
        """

        :param x: int
        :return: int
        """
        # int型的最大值判断
        if(x == 2**32): return 0
        negative = 1
        # 判断x的正负
        if(x < 0):
            x = -x
            negative = -1
        strNum = str(x)
        num1 = int(strNum[::-1])
        if num1 >= 2 ** 32:
            return 0
        else:
            return num1 * negative