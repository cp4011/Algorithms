"""给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。
示例 1:
输入: [3,2,3]
输出: 3
示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
"""

class Solution:
    def majorityElement(self, nums):    # 时间复杂度：O(nlgn)
        nums.sort()                     # 排序法
        return nums[len(nums)//2]

class Solution:
    def majorityElement(self, nums):
        import collections
        counts = collections.Counter(nums)  # 哈希表法
        return max(counts.keys(), key=counts.get)   # key关键字，对每个tlist元素先使用key指定的function来处理，然后再比较、返回预期tlist中的数