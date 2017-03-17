# _*_ coding: utf-8 _*_

# @Time     :2017.3.8 下午 5:09
# @Author   :ZuMing Shen
# File      :Adjust_sort.py
# software  :PyCharm


from sort_algorithm import Array_generate


def adjust_sort(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_sort(lists, max, size)


def build_heap(lists, size):
    for i in range(0, (size/2))[::-1]:
        adjust_sort(lists, i, size)


def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_sort(lists, 0, i)