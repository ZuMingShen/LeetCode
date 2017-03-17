# _*_ coding: utf-8 _*_

# @Time     :2017.3.12 下午 9:24
# @Author   :ZuMing Shen
# File      :1.Two Sum.py
# software  :PyCharm


class Solution1(object):
    def twosum(self, nums, target):
        lists = []
        L = len(nums)
        for i in range(L):
            for j in range(i, L):
                if nums[i] + nums [j] == target:
                    lists.append(i)
                    lists.append(j)
        return lists


class Solution2(object):
    def twosum(nums, target):
        dict = {}
        [dict.setdefault(x, y) for x, y in enumerate(nums)]
        key_list = []
        value_list = []
        lists = []
        for key, value in dict.items():
            key_list.append(key)
            value_list.append(value)
        for i in range(len(key_list)):
            num = target - value_list[i]
            print('num:%d'%num)
            if num in value_list[i+1::]:
                a = value_list[i+1::]
                print(a)
                j = a.index(num)
                print(j+1+i)
                lists.append(i)
                lists.append(j+1+i)
        print(lists)

list1 = [3, 3]
twosum(list1, 6)


