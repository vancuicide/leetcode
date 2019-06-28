# -*-coding:utf-8-*-

# Link: https://leetcode.com/problems/combination-sum/

# Problem Description:
# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# Example:
# candidates = [2,3,6,7], target = 7
# Result:
# [
#   [7],
#   [2,2,3]
# ]
# Example:
# candidates = [2,3,5], target = 8
# Result:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

# 思路：找一个临时数组存储当前遍历到的数字，判断该数组之和与target是否相等，不相等就不是待选


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, index, path, res):
        """
        运行策略，尽可能先往path里面加数，如果path之和大于target，不处理并跳出，然后再慢慢加大数
        原则：只要path之和不超过target，就一直加，因为加小的数不容易超，所以先加小的数的部分就一直在递归，直到target<0
        :param candidates: 所给数组
        :param target: 目标结果，这里可采用纳入一个进path就改变target的方法
        :param index: 遍历索引，防止重复，要保证path之间不重复
        :param path: 记录符合条件的结果
        :param res: 总结果
        :return: None，res已经记录了结果
        """
        if target < 0:  # 证明此时已没有合适的candidates，跳出递归
            return
        if target == 0:  # 当前path的和等于target
            res.append(path)
            return
        for i in range(index, len(candidates)):
            self.dfs(candidates, target-candidates[i], i, path+[candidates[i]], res)  # 更新target和path，进行下一次递归


if __name__ == '__main__':
    solution = Solution()
    # test case:
    # candidates = [2,3,6,7], target = 7
    # return:
    # [
    #   [7],
    #   [2,2,3]
    # ]
    # test case:
    # candidates = [2,3,5], target = 8
    # return:
    # [
    #   [2,2,2,2],
    #   [2,3,3],
    #   [3,5]
    # ]
    print(solution.combinationSum([2, 3, 6, 7], 7))
    print(solution.combinationSum([2, 3, 5], 8))

