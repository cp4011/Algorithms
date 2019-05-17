"""给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""


class Solution:
    def combinationSum2(self, candidates, target):
        """ (candidates: List[int], target: int) -> List[List[int]] candidates 中的每个数字在每个组合中只能使用一次。"""
        if not candidates or min(candidates) > target:
            return []
        candidates.sort()
        res = []

        def dfs(candidates, target, temp_list):
            if target == 0:
                res.append(temp_list)
                return
            if target < 0:
                return
            for i in range(len(candidates)):
                if candidates[i] > target:
                    continue
                # candidates中的每个数字在每个组合中只能使用一次,组合：candidates[i+1:]
                dfs(candidates[i+1:], target-candidates[i], temp_list + [candidates[i]])

        dfs(candidates, target, [])
        return list(map(list, set(tuple(l) for l in res)))      # 对嵌套列表res去重,列表list不能被哈希，转成tuple元组被集合hash
        # d = {}                      # 利用字典对嵌套列表res去重
        # for l in res:
        #     if tuple(l) not in d:   # 列表list不能被哈希，转成tuple元组作为字典的 键
        #         d[tuple(l)] = 1
        # return [list(i) for i in d.keys()]

    def combinationSum2_1(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, tmp_sum, tmp_list):
            if tmp_sum == target:
                res.append(tmp_list)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target: break
                if j > i and candidates[j] == candidates[j - 1]: continue
                backtrack(j + 1, tmp_sum + candidates[j], tmp_list + [candidates[j]])   # candidates中的每个数字在每个组合中只能使用一次

        backtrack(0, 0, [])
        return res
