# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/container-with-most-water/

# Problem Description:
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
#  n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.

# Example:
# [1,8,6,2,5,4,8,3,7]
# return 49.

# 思路：从两边往中间计算蓄水量，并用一个单元记录这个最大值


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        maxWater = 0
        while left < right:
            low = min(height[left], height[right])
            current = low * (right - left)
            if current > maxWater:  # 更新蓄水值
                maxWater = current
            if height[left] > height[right]:  # 区间更新策略
                right -= 1
            else:
                left += 1
        return maxWater


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # [1,8,6,2,5,4,8,3,7]
    # return:
    # 49
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

