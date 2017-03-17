# _*_ coding: utf-8 _*_

# @Time     :2017.3.12 下午 7:40
# @Author   :ZuMing Shen
# File      :461.Hamming Distance.py
# software  :PyCharm


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = bin(x)
        b = bin(y)
        a1 = a[:1-len(a):-1]
        b1 = b[:1-len(b):-1]
        A, B = [], []
        count = 0
        for i in a1:
            A.append(i)
        for j in b1:
            B.append(j)
        Len = len(A) - len(B)
        if Len < 0:
            for i in range(abs(Len)):
                A.append('0')
        else:
            for i in range(abs(Len)):
                B.append('0')
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
        return count