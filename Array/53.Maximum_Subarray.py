# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/maximum-subarray/

# Problem Description:
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

# Example:
# [-2,1,-3,4,-1,2,1,-5,4]
# Result:
# 6
# Explanation:
# [4,-1,2,1] has the largest sum = 6.


# 思路：用一个值cur来表示当前的遍历值之前的和，如果该和小于0，即可抛弃之前的，因为还不如当前遍历值


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 容错
        if not nums:
            return 0
        maxx = float('-inf')
        cur = 0
        for num in nums:
            if cur <= 0:
                cur = num
            else:
                cur += num
            if cur > maxx:
                maxx = cur
        return maxx


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # Result:
    # 6
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.maxSubArray([3, 4, -1, 1]))
    print(solution.maxSubArray([7, 8, 9, 11, 12]))

