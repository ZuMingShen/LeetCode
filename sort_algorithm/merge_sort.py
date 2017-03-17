# _*_ coding: utf-8 _*_

# @Time     :2017.3.9 下午 7:44
# @Author   :ZuMing Shen
# File      :merge_sort.py
# software  :PyCharm


from sort_algorithm import Array_generate


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = int(len(lists) / 2)
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


def main():
   L = Array_generate.array_generate()
   A = merge_sort(L)


if __name__ == '__main__':
    main()
