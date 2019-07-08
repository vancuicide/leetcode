# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/plus-one/

# Problem Description:
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list,
# and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# 思路：


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, len(digits)-1-i)
        return [int(i) for i in str(num+1)]


if __name__ == '__main__':
    # Example:
    # Input: [1,2,3]
    # Output: [1,2,4]
    print(Solution().plusOne([1, 2, 3]))
    # Input: [4,3,2,1]
    # Output: [4,3,2,2]
    print(Solution().plusOne([4, 3, 2, 1]))



