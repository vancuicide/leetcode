# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/first-missing-positive/

# Problem Description:
# Given an unsorted integer array, find the smallest missing positive integer.
# Notes:
# Your algorithm should run in O(n) time and uses constant extra space.

# Example:
# [1,2,0]
# Result:
# 3
# Example:
# [3,4,-1,1]
# Result:
# 2
# Example:
# [7,8,9,11,12]
# Result:
# 1

# 思路：题目说要求O(n)时间复杂度，没有想出来，查了一下list.sort()的复杂度，O(n log n)，那就排个序，挨个看就行


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        unseen = 1
        for num in nums:
            if num > unseen:  # 中间缺失数值的情况
                return unseen
            elif num == unseen:
                unseen += 1  # 可能是后面缺失的情况
        return unseen


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # [1,2,0]
    # Result:
    # 3
    # test case:
    # [3,4,-1,1]
    # Result:
    # 2
    # test case:
    # [7,8,9,11,12]
    # Result:
    # 1
    print(solution.firstMissingPositive([1, 2, 0]))
    print(solution.firstMissingPositive([3, 4, -1, 1]))
    print(solution.firstMissingPositive([7, 8, 9, 11, 12]))

