# _*_ coding: utf-8 _*_

# @Time     :2017.3.6 下午 9:36
# @Author   :ZuMing Shen
# File      :Shell_sort.py
# software  :PyCharm

from sort_algorithm import Array_generate


def shell_sort(lists):
    count = len(lists)
    step = 2
    group = int(count / step)
    while group > 0:
        for i in range(group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k = k - group
                j = j + group
        group = int(group / step)  # The type of 'group' is float, if do not use intp
    print(lists)


def main():
    shell_sort(Array_generate.array_generate())


if __name__ == '__main__':
    main()


