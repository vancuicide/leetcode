# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Problem Description:
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].

# Example:
# nums = [5,7,7,8,8,10], target = 8
# Result:
# [3,4]
# Example:
# nums = [5,7,7,8,8,10], target = 6
# Result:
# [-1,-1]

# 思路：需要培养一个意识，就是遇见排序数组，先想到二分法；另一个意识，就是遇见log n，还是先想到二分法


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 异常处理
        if len(nums) <= 0:
            return [-1, -1]

        left = 0; right = len(nums)-1
        # 先去寻找第一个
        while left <= right:
            mid = (left + right) >> 1
            # 判断
            if nums[mid] >= target:  # 证明第一个还在左边
                right = mid - 1
            else:
                left = mid + 1
        begin = left  # 保留第一个位置

        left = 0; right = len(nums) - 1
        # 再去找最后一个
        while left <= right:
            mid = (left + right) >> 1
            # 判断
            if nums[mid] <= target:  # 证明最后一个还在右边
                left = mid + 1
            else:
                right = mid - 1
        end = right  # 保留最后一个位置

        # 合理性校验
        if begin <= end:
            return [begin, end]
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # nums = [4,5,6,7,0,1,2], target = 0
    # return:
    # 4
    # test case:
    # nums = [4,5,6,7,0,1,2], target = 3
    # return:
    # -1
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))
