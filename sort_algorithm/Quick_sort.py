# _*_ coding: utf-8 _*_

# @Time     :2017.3.7 上午 10:16
# @Author   :ZuMing Shen
# File      :Quick_sort.py
# software  :PyCharm


from sort_algorithm import Array_generate


def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left -= 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    print(lists)


L = Array_generate.array_generate()


def main():
    quick_sort(L, 0, len(L)-1)


if __name__ == '__main__':
    main()
