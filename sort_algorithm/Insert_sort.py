# _*_ coding: utf-8 _*_

# @Time     :2017.3.5 下午 2:57
# @Author   :ZuMing Shen
# File      :Insert_sort.py
# software  :PyCharm

from sort_algorithm import Array_generate


def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j = j - 1
    print(lists)


def main():
    insert_sort(Array_generate.array_generate())


if __name__ == '__main__':
    main()
