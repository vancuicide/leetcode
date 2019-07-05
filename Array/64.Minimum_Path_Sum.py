# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/minimum-path-sum/

# Problem Description:
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

# Example:
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

# 思路：dp思想，用一个cost矩阵记录走到每个位置需要的最小代价，其中左上角为就是当前代价，0行0列也都只和其之前的有关


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 容错
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        cost = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    cost[i][j] = grid[i][j]
                elif i == 0:
                    cost[i][j] = cost[i][j-1] + grid[i][j]
                elif j == 0:
                    cost[i][j] = cost[i-1][j] + grid[i][j]
                else:
                    cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j]
        return cost[m-1][n-1]


if __name__ == '__main__':
    # Input:
    # [
    #   [1,3,1],
    #   [1,5,1],
    #   [4,2,1]
    # ]
    # Output: 7
    print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))



