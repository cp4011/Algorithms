"""给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:
输入: nums = [1], k = 1
输出: [1]
说明：
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
"""
'''1. 建立一个元素值对应出现频率的哈希表,用collections中的Counter构建需要的哈希表，然后sorted(iterable,key=,reverse=True)[:n]'''

'''2. 建立堆，堆中添加一个元素的复杂度是 O(log(k)),时间复杂度：O(Nlog(k))'''


class Solution:
    def topKFrequent(self, nums, k):
        import collections
        import heapq
        count = collections.Counter(nums)  # heapq.nlargest(n, iterable, key=None)等价 sorted(iterable, key=key, reverse=True)[:n]
        return heapq.nlargest(k, count.keys(), key=count.get)   # 关键字key后是个函数，作用于iterable中的每一个元素，如key=str.lower