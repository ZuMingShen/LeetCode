# _*_ coding: utf-8 _*_

# @Time     :2017.3.6 下午 10:33
# @Author   :ZuMing Shen
# File      :Bubble_sort.py
# software  :PyCharm

from sort_algorithm import Array_generate


def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    print(lists)


def main():
    bubble_sort(Array_generate.array_generate())


if __name__ == '__main__':
    main()
