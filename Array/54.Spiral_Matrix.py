# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/spiral-matrix/

# Problem Description:
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Result:
# [1,2,3,6,9,8,7,4,5]


# 思路：顺时针打印矩阵


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 容错
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])

        result = []

        left, right, top, bottom = 0, cols-1, 0, rows-1
        while left <= right and top <= bottom:
            for i in range(left, right+1):  # 上行
                result.append(matrix[top][i])
            for i in range(top+1, bottom+1):  # 右列
                result.append(matrix[i][right])
            if top != bottom:  # 如果存在最下一行
                for i in range(left, right)[::-1]:
                    result.append(matrix[bottom][i])
            if left != right:  # 如果存在最左边一列
                for i in range(top+1, bottom)[::-1]:
                    result.append(matrix[i][left])
            # 相当于走了一圈，要收缩了
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # [
    #  [ 1, 2, 3 ],
    #  [ 4, 5, 6 ],
    #  [ 7, 8, 9 ]
    # ]
    # Result:
    # [1,2,3,6,9,8,7,4,5]

    # test case:
    # [
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8],
    #     [9, 10, 11, 12]
    # ]
    # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    print(solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))


