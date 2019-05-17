"""给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1
说明: 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
"""
'''把数组的索引号利用起来,把位置0放数字1,位置1放数字2...就可以节省存储索引的空间了,按照这样的方法重新整理数组,再扫一次就能知道答案了.
比如示例中的:[3,4,-1,1]
第一步,数字3它应该放在位置2 ,交换位置,[-1,4,3,1]
第二步,数字4应该放在位置3,交换位置,[-1,1,3,4],此时有个关键,数字1应该在位置0,所以我们继续交换,[1,-1,3,4]
...
我们再次扫数组,就能得到结果.
所以,时间复杂度:O(2n),空间复杂度:O(1)'''


class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)                   # 输入: [3,4,-1,1]
        for i in range(n):
            # 注意是while，不是if【一直要将索引为0的位置 放1 或索引0的位置上的数不在[1,n]之间为止，此时也不能作为索引】
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:    # 索引为0时，第一轮互换后：[-1,4,3,1] 第二轮：无
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # 索引为0时，第一轮互换后：[-1,1,3,4] 第二轮：[1,-2,3,4]
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]   超时
        i = 0
        while i < n and i + 1 == nums[i]:
            i += 1
        return i + 1        # 返回没出现的最小的正整数
