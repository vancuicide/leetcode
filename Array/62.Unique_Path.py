# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/unique-paths/

# Problem Description:
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

# Example:
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
#
# Input: m = 7, n = 3
# Output: 28

# 思路：右下角的数字代表可以过来的路的条数


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if m == 1 and n == 1:
            return 1
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 1 and j == 0:
                    dp[i][j] = 1
                elif i == 0 and j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


if __name__ == '__main__':
    # Input: m = 3, n = 2
    # Output: 3
    print(Solution().uniquePaths(3, 2))

    # Input: m = 7, n = 3
    # Output: 28
    print(Solution().uniquePaths(7, 3))


