# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/spiral-matrix-ii/

# Problem Description:
# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# Example:
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

# 思路：先创立一个n*n的数组，然后按照顺时针顺序往里面加数，用needle记录


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        result = [[0 for _ in range(n)] for _ in range(n)]
        needle = 1
        left, right, top, bottom = 0, n-1, 0, n-1
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                result[top][i] = needle
                needle += 1
            for i in range(top+1, bottom+1):
                result[i][right] = needle
                needle += 1
            if top != bottom:
                for i in range(left, right)[::-1]:
                    result[bottom][i] = needle
                    needle += 1
            if left != right:
                for i in range(top+1, bottom)[::-1]:
                    result[i][left] = needle
                    needle += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return result


if __name__ == '__main__':
    # Input: 3
    # Output:
    # [
    #  [ 1, 2, 3 ],
    #  [ 8, 9, 4 ],
    #  [ 7, 6, 5 ]
    # ]
    print(Solution().generateMatrix(3))
    # Input: 4
    # Output:
    # [
    #  [ 1, 2, 3, 4 ],
    #  [ 12, 13, 14, 5 ],
    #  [ 11, 16, 15, 6 ],
    #  [ 10, 9, 8, 7]
    # ]
    print(Solution().generateMatrix(4))


