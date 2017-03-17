# _*_ coding: utf-8 _*_

# @Time     :2017.3.7 下午 5:05
# @Author   :ZuMing Shen
# File      :Select_sort.py
# software  :PyCharm

from sort_algorithm import Array_generate


def select_sort(lists):
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i+1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    print(lists)


def main():
    select_sort(Array_generate.array_generate())


if __name__ == '__main__':
    main()