"""在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""

""" 排序法
最朴素的方法是先对数组进行排序，再返回倒数第 k 个元素，就像 Python 中的 sorted(nums)[-k]。 
算法的时间复杂度为O(NlogN)，空间复杂度为O(1)。这个时间复杂度并不令人满意，让我们试着用额外空间来优化时间复杂度。

堆
思路是创建一个大顶堆，将所有数组中的元素加入堆中，并保持堆的大小小于等于 k。这样，堆中就保留了前 k 个最大的元素。
这样，堆顶的元素就是正确答案。
像大小为 k 的堆中添加元素的时间复杂度为 O(logk)，我们将重复该操作 N 次，故总时间复杂度为O(Nlogk)。
在 Python 的 heapq 库中有一个 nlargest 方法，具有同样的时间复杂度，能将代码简化到只有一行。
本方法优化了时间复杂度，但需要 O(k) 的空间复杂度
"""


"""o(nlgk)时间复杂度的分治方法
当数组长度>2k,从中间切成两部分，分别求最大的k个元素列表，然后两路归并回来。
当数组长度<=2K,用排序求最大的k个元素列表
时间复杂度o(nlgk),当n>>k时比直接排序o(nlgn)好。"""
class Solution:
    def findKthLargest(self, nums, k):    # o(nlgk)时间复杂度的分治方法
        def helper(num, k):
            if len(num) <= 2 * k:
                num = sorted(num, key=lambda x: -x)
                return num[:k]
            else:
                m = len(num) // 2       # 如果数组长度大于2k，切成两半分别求最大的k个元素
                L = helper(num[:m], k)
                R = helper(num[m:], k)
                ans = []                # 两路归并
                l = 0
                r = 0
                while l + r < k:
                    if L[l] > R[r]:
                        ans.append(L[l])
                        l += 1
                    else:
                        ans.append(R[r])
                        r += 1
                return ans
        fk = helper(nums, k)
        return fk[-1]

    def findKthLargest1(self, nums, k):
        import heapq
        return heapq.nlargest(k, nums)[-1]
