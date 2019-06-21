# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/3sum/

# Problem Description:
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

# Example:
# [-1, 0, 1, 2, -1, -4]
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# 思路：先排序，预先卡一个数，以它为基准往后数，剩下的数从两头往中间夹，判断三个数的和与0的大小关系，重复的数应该跳过


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        length = len(nums)
        nums.sort()
        for i in range(0, length-2):
            if nums[i] > 0:  # 如果遍历的值已经大于0，也没必要看之后的值了
                break
            if i > 0 and nums[i-1] == nums[i]:  # 如果卡的这个数重复了，就直接跳过
                continue
            l = i+1  # 从两头往中间夹
            r = length-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    # 证明当前和比较小，要增大l对应的值
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # 这两个while是为了去除重复值
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    # 下面两个是为了还能有机会让和等于0
                    l += 1
                    r -= 1

        return res


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # [-1, 0, 1, 2, -1, -4]
    # return:
    # [[-1, 0, 1], [-1, -1, 2]]
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))

