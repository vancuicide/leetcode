# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Problem Description:
# Given a sorted array nums, remove the duplicates in-place such that each element
# appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array
# in-place with O(1) extra memory.

# Example:
# nums = [1,1,2].
# 就地删除，结果为：[1, 2]

# 思路：这道题很简单，唯一要求就是就地删除，所以需要有一个指针，确保每一个元素都经过了“某种”操作（不重复，指针后移；重复，就地删除），
# 都保留第一个未出现元素


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        while index < len(nums)-1:
            if nums[index] == nums[index+1]:
                del nums[index+1]
            else:
                index += 1
        return nums


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # [1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # return:
    # [1, 2], [0, 1, 2, 3, 4]  # with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
    print(solution.removeDuplicates([1, 1, 2]))
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

