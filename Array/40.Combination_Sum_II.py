# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/combination-sum-ii/

# Problem Description:
# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
# Each number in candidates may only be used once in the combination.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# Example:
# candidates = [10,1,2,7,6,1,5], target = 8
# Result:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example:
# candidates = [2,5,2,1,2], target = 5
# Result:
# [
#   [1,2,2],
#   [5]
# ]

# 思路：本题和上题不同点在于这里的数不能重复取，而且需要避免相同path都被加进去的情况


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        print(candidates)
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:  # 避免了考虑两个[1]的情况，这样可以避开重复出现的情况，一般是一个数的时候
                continue
            if candidates[i] > target:
                break
            self.dfs(candidates, target-candidates[i], i+1, path+[candidates[i]], res)  # 这里index直接加一，防止重复取，但需要判别加一后的数是否有和之前一样的


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # candidates = [10,1,2,7,6,1,5], target = 8
    # return:
    # [
    # [1, 7],
    # [1, 2, 5],
    # [2, 6],
    # [1, 1, 6]
    # ]
    # test case:
    # candidates = [2,5,2,1,2], target = 5
    # return:
    # [
    # [1,2,2],
    # [5]
    # ]
    print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(solution.combinationSum2([2, 5, 2, 1, 2], 5))

