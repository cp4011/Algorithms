"""输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""
import heapq            # 小顶堆


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput) or k < 0 or not tinput:      # 注意边界k，以及有not
            return []
        heapq.heapify(tinput)                           # 在原数组上构建堆
        return heapq.nsmallest(k, tinput)               # 输出最小k个数
