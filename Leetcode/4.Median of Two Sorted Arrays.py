# _*_ coding: utf-8 _*_

# @Time     :2017.3.21 下午 4:28
# @Author   :ZuMing Shen
# File      :4.Median of Two Sorted Arrays.py
# software  :PyCharm


class Solution(object):
    def getKth(self, num1, num2, k):
        len1 = len(num1)
        len2 = len(num2)
        if len1 > len2:
            return self.getKth(num2, num1, k)
        if len1 == 0:
            return num2[k-1]
        if k == 1:
            return min(num1[0], num2[0])
        pa = min(k/2, len1)
        pb = k - pa
        if num1[pa-1] <= num2[pb-1]:
            return self.getKth(num1[pa:], num2, pb)
        else:
            return self.getKth(num1, num2[pb:], pa)
        
    def findMedianSortedArrays(self, nums1, nums2):
        """

        :param nums1: List[int]
        :param nums2: List[int]
        :return:      float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, nums2, (len1 + len2)/2 +1)
        else:
            return (self.getKth(nums1, nums2, (len1+len2)/2) + self.getKth(nums1, nums2, (len1+len2)/2 + 1)) * 0.5

