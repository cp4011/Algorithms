"""最小的K个数
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""
''' *基于堆排序算法，构建最大堆。时间复杂度为O(nlogk)
    *如果用快速排序，时间复杂度为O(nlogn)；
    *如果用冒泡排序，时间复杂度为O(n*k)
'''

# 牛客网支持  小顶堆heapq.heapify(list)  heapq.heappush(list,2)  heapq.heappop(list)弹出最小值 heapq.heapreplace(list,99)  heapq.nlargest(3,list)
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, k, tinput):
        if k > len(tinput):
            return []
        return heapq.nsmallest(k, tinput)

# 直接排序
def GetLeastNumbers_Solution(input, k):
    if k > len(input):
        return []
    return sorted(input)[0:k]
