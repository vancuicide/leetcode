# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/two-sum/

# Problem Description:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# 思路：要返回两个值之和等于target的索引，当遍历到某个数值时，可以判断 target和它的差 是否已经存在，如果存在，就返回两者，否则记录当前值


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        appeared_ = dict()  # 记录出现的数字和索引，用字典
        for index, num in enumerate(nums):
            sub = target - num
            if sub in appeared_:
                return [appeared_[sub], index]
            else:
                appeared_[num] = index


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # [2, 7, 11, 15], target = 9
    # return:
    # [0, 1]
    print(solution.twoSum([2, 7, 11, 15], 9))

