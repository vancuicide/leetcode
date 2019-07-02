# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/jump-game/

# Problem Description:
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

# Example:
# [2,3,1,1,4]
# Result:
# true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example:
# [3,2,1,0,4]
# Result:
# false
# Explanation: You will always arrive at index 3 no matter what.
#  Its maximum jump length is 0, which makes it impossible to reach the last index.


# 思路：用一个能量值来记录可以跳过的最远距离，这个距离应该是当前位置与该位置的能量之和，与nums的长度比


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jumpPower = 0  # 用于记录当前最大跳跃值
        for i in range(len(nums)):
            if i > jumpPower:
                break  # 证明当前的位置已经跳不过去了，不用考虑了
            jumpPower = max(i + nums[i], jumpPower)  # 更新最大跳跃值
        return jumpPower >= len(nums)-1  # 判断最大跳跃值能否跳到最后


if __name__ == '__main__':
    solution = Solution()
    # Example:
    # [2,3,1,1,4]
    # Result:
    # true

    # Example:
    # [3,2,1,0,4]
    # Result:
    # false
    print(solution.canJump([2, 3, 1, 1, 4]))
    print(solution.canJump([3, 2, 1, 0, 4]))


