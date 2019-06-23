# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/4sum/

# Problem Description:
# Given an array nums of n integers and an integer target,
# are there elements a, b, c, and d in nums such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.

# Example:
# nums = [1, 0, -1, 0, -2, 2], and target = 0.
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# 思路：其实和3Sum差不多，只不过需要遍历两个数i,j，再去拿两个数夹


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        length = len(nums)
        nums.sort()
        for i in range(0, length-3):
            if i > 0 and nums[i] == nums[i-1]:  # 避免i遇到相同的数
                continue
            for j in range(i+1, length-2):
                if j > i + 1 and nums[j] == nums[j-1]:  # 避免j遇到相同的数
                    continue
                l = j+1
                r = length-1
                while l < r:
                    summ = nums[i] + nums[j] + nums[l] + nums[r]
                    if summ == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:  # 避免l遇到相同的数
                            l += 1
                        while l < r and nums[r] == nums[r-1]:  # 避免r遇到相同的数
                            r -= 1
                        # 如果当前和等于target，那么必须同步l和r，即增加l减小r，才有可能再次让和等于target
                        l += 1
                        r -= 1
                    elif summ > target:
                        r -= 1
                    else:
                        l += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # nums = [1, 0, -1, 0, -2, 2], and target = 0.
    # return:
    # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))

