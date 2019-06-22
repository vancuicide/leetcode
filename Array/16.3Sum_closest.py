# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/3sum-closest/

# Problem Description:
# Given an array nums of n integers and an integer target,
# find three integers in nums such that the sum is closest to target. Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example:
# [-1, 2, 1, -4], target = 1
# A solution set is:
# 2 (-1 + 2 + 1 = 2)

# 思路：先排序，预先卡一个数，以它为基准往后数，剩下的数从两头往中间夹，判断三个数的和与0的大小关系，重复的数应该跳过
# 这个题和15题的差别就是，有可能当前的和不等于target，这时需要记录和target最接近的数


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = nums[0] + nums[1] + nums[2]  # 用来表示当前最接近target的数
        length = len(nums)
        nums.sort()
        for i in range(0, length-2):
            l = i+1
            r = length-1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == target:  # 如果当前遍历和等于目标值
                    return summ
                if abs(summ - target) < abs(result - target):  # 如果当前遍历和summ比result更接近target
                    result = summ
                if summ < target:  # 看遍历和与target具体大小关系
                    l += 1
                else:
                    r -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # [-1, 2, 1, -4], 1
    # return:
    # 1
    print(solution.threeSumClosest([-1, 2, 1, -4], 1))

