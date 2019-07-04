# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/unique-paths-ii/

# Problem Description:
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# Example:
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

# 思路：由于路上有阻隔，所以可从终点往回算，遇到阻隔将路的条数置为0


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        # 从终点出发，看有多少条路径可以到初始点，dp[i][j]表示到当前这个点有几种方法，dp[i][j]的方法总数就等于dp[i+1][j]加dp[i][j+1]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == m-1 or j == n-1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]


if __name__ == '__main__':
    # Input:
    # [
    #   [0,0,0],
    #   [0,1,0],
    #   [0,0,0]
    # ]
    # Output: 2
    print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))



