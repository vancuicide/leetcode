# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/insert-interval/

# Problem Description:
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.

# Example:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


# 思路：本题已经进行了排序，只需要把新区间也加进来，然后综合排序，即可像上一道题一样处理


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals = intervals + [newInterval]
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for n in intervals[1:]:
            # 有重叠
            if res[-1][1] >= n[0]:
                res[-1][1] = max(res[-1][1], n[1])
            else:  # 无重叠
                res.append(n)
        return res


if __name__ == '__main__':
    # Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    # Output: [[1,5],[6,9]]
    print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
    # Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    # Output: [[1,2],[3,10],[12,16]]
    print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))


