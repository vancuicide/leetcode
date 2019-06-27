# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/search-insert-position/

# Problem Description:
# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

# Example:
# [1,3,5,6], 5
# Result:
# 2
# Example:
# [1,3,5,6], 2
# Result:
# 1

# 思路：在一个排序数组中，遍历每一个数字，如果这个数字比target小，直到找到第一个比target大的元素，这时记录index，既是target应该插入的位置


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 特殊情况考虑
        if len(nums) == 0:  # 当前数组无数字
            return 0
        if len(nums) == 1:  # 当前数组有一个数字，比较这两个数的大小
            if target < nums[0]:
                return 0
            else:
                return 1
        result = -1
        for index, item in enumerate(nums):
            if nums[index] >= target and result < 0:  # 判断：找到第一个比target的数字，用result的正负标识是否标记过result
                result = index
        # 这时有两种情况，(1)找到了第一个比target大的元素，此时result >= 0；(2)没有找到，即result还是小于0的
        if result >= 0:
            return result
        else:
            return len(nums)


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # [1,3,5,6], 5
    # return:
    # 2
    # test case:
    # [1,3,5,6], 2
    # return:
    # 1
    print(solution.searchInsert([1, 3, 5, 6], 5))
    print(solution.searchInsert([1, 3, 5, 6], 2))
    print(solution.searchInsert([1, 3, 5, 6], 7))
    print(solution.searchInsert([1, 3, 5, 6], 0))

