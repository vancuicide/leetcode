# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/set-matrix-zeroes/

# Problem Description:
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Example:
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
#
# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]

# 思路：


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 要先处理矩阵内部的（通过最外面行列标记），然后再处理最外面的，因为最外面的置0会影响所有值
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        # ----------------统计0行0列是否原有0，这一部分不能先处理，因为会影响所有的！！
        row_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                row_zero = True
        col_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                col_zero = True
        # -------------------------------------------------------------------

        # ----------------开始统计矩阵内部的数据，如果(i, j)是0，就把最外面的置0
        for i in range(1, m):  # 从1开始看，因为从0开始的话，会重复计算（把第0行都置0了，所有列也都成了0）
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # 把第0行的第一个置为0
                    matrix[0][j] = 0
        # -------------------------------------------------------------------

        # -----------------根据最外面0行0列开始对整行整列进行置0
        for i in range(1, m):  # 从1开始看
            if matrix[i][0] == 0:  # 上面某行的第一个被置为0，证明这一行是有0的
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        # ------------------------------------------------------------------

        # -----------------最后处理的是一开始为0的
        if col_zero:
            for j in range(n):
                matrix[0][j] = 0
        if row_zero:
            for i in range(m):
                matrix[i][0] = 0

        return matrix


if __name__ == '__main__':
    # Example:
    # Input:
    # [
    #   [1,1,1],
    #   [1,0,1],
    #   [1,1,1]
    # ]
    # Output:
    # [
    #   [1,0,1],
    #   [0,0,0],
    #   [1,0,1]
    # ]
    print(Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    # Input:
    # [
    #   [0,1,2,0],
    #   [3,4,5,2],
    #   [1,3,1,5]
    # ]
    # Output:
    # [
    #   [0,0,0,0],
    #   [0,4,5,0],
    #   [0,3,1,0]
    # ]
    print(Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))



