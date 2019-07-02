# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/merge-intervals/

# Problem Description:
# Given a collection of intervals, merge all overlapping intervals.

# Example:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example:
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.


# 思路：用一个数组res来记录结果，先将所有小区间按头排序，然后进行合并，合并原则是res最后一个区间的末尾要比待排序的第一个区间的头部大，
# 其余就属于没有交集


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # 这里没有把列表输入的内容转换成interval类，所以只能用list的性质来进行比对
        # 容错
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for n in intervals[1:]:
            if res[-1][1] > n[0]:  # 更新规则：如果最后一个区间的尾部大于待加入区间的头部
                res[-1][1] = max(res[-1][1], n[1])
            else:  # 更新规则：区间无交叉
                res.append(n)
        return res


if __name__ == '__main__':
    # Input: [[1,3],[2,6],[8,10],[15,18]]
    # Output: [[1,6],[8,10],[15,18]]
    print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    # Input: [[1,4],[4,5]]
    # Output: [[1,5]]
    print(Solution().merge([[1, 4], [4, 5]]))


