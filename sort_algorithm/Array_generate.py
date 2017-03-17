# _*_ coding: utf-8 _*_

# @Time     :2017.3.6 下午 9:37
# @Author   :ZuMing Shen
# File      :Array_generate.py
# software  :PyCharm


def array_generate():
    n = int(input("Please input the length of the array："))
    A = []
    for i in range(1, n+1):
        nums = int(input("Please input the %d numbers：" %i))
        A.append(nums)
    return A

