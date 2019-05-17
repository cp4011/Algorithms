"""给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

'''回溯算法:不合适就退回上一步,然后通过约束条件, 减少时间复杂度.
39.组合总和  40. 组合总和 II  46. 全排列  47. 全排列 II   78. 子集  90. 子集 II
这类题目都是同一类型的,用回溯算法!
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """ :type candidates: List[int]  :type target: int  :rtype: List[List[int]]  candidates中的数字可以无限制重复被选取"""
        if not candidates or min(candidates) > target:
            return []
        # candidates.sort()
        res = []

        def dfs(candidates, target, temp_list):
            if target == 0:
                res.append(temp_list)
                return
            if target < 0:
                return
            for i in range(len(candidates)):
                if candidates[i] > target:
                    continue                    # 也可以candidates.sort()，这里就是 break
                # 题意：无重复元素的数组candidates中的数字可以无限制重复被选取，不是candidates[i+1:]
                dfs(candidates[i:], target - candidates[i], temp_list + [candidates[i]])     # 组合 candidates[i:]

        dfs(candidates, target, [])      # 调用
        return res


# 回溯算法标准模板
def combinationSum(candidates, target):
    """(candidates: List[int], target: int) -> List[List[int]]"""
    candidates.sort()
    n = len(candidates)
    res = []

    def helper(i, tmp_sum, tmp):
        if tmp_sum > target or i == n:
            return
        if tmp_sum == target:
            res.append(tmp)
            return
        helper(i,  tmp_sum + candidates[i], tmp + [candidates[i]])
        helper(i+1, tmp_sum, tmp)

    helper(0, 0, [])
    return res
