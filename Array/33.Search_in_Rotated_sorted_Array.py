# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

# Problem Description:
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

# Example:
# nums = [4,5,6,7,0,1,2], target = 0
# Result:
# 4
# Example:
# nums = [4,5,6,7,0,1,2], target = 3
# Result:
# -1


# 思路：这里是一个排序好的数组，然后旋转了一波；题目中有要求时间复杂度是O(log n)，所以还是采用二分法，但是在判别过程中需要加一些内容


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not len(nums):
            return -1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) >> 1
            if target == nums[mid]:  # 循环跳出条件，即找到相等的，否则就更新左右两个index
                return mid
            if nums[left] <= nums[mid]:  # 证明此时left到mid是一个递增序列，即处在大的数部分，(!)关键在于找到一个递增序列
                if nums[left] <= target <= nums[mid]:  # 判断target是否在里面
                    right = mid-1
                else:
                    left = mid+1
            else:  # 证明mid在后面，此时mid到right是一个递增序列，即处在小的数部分，(!)关键在于找到一个递增序列
                if nums[mid] <= target <= nums[right]:  # 判断target是否在里面
                    left = mid+1
                else:
                    right = mid-1
        return -1


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # nums = [4,5,6,7,0,1,2], target = 0
    # return:
    # 4
    # test case:
    # nums = [4,5,6,7,0,1,2], target = 3
    # return:
    # -1
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
