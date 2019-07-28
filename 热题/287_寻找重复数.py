"""给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有
一个重复的整数，找出这个重复的数。
示例 1:
输入: [1,3,4,2,2]
输出: 2
示例 2:
输入: [3,1,3,4,2]
输出: 3
说明：
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
"""


class Solution:  # 一个包含n+1个整数的数组nums，其数字都在1到n之间（包括1和n），可知至少存在一个重复的整数。假设只有一个重复的整数
    def findDuplicate(self, nums):      # 弗洛伊德的乌龟和兔子（循环检测）【时间复杂度O(n)，时间复杂度O(1)】
        '''一个n+1大小的数组，数组内的元素为1~n,我们用1个索引对应一个相应的数字，例如数字1对应index1，那么肯定有多个数字
        对应了同一个index，那么这个index就是我们要找的重复数
        因为我们不能用额外的空间，我们可以将这个特殊的数组想像成这样一个链表这个数据结构，链表结点的value为数组值，而同时
        链表的value又指向下一个链表结点。那么我们的问题可以抽象为在链表中找环的入口问题，使用一个fast指针和一个slow指针，
        先找到在环内的交点，然后从起点开始，和交点一起按照步长为1运动，最后的交点就是我们要找到重复数字'''
        slow, fast, start = 0, 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:        # 快慢指针相遇
                break
        while start != slow:        # 直到两指针相交
            start = nums[start]
            slow = nums[slow]
        return start

    def findDuplicate1(self, nums):      # 哈希法【时间复杂度O(n)，空间复杂度O(n)】
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

    def findDuplicate2(self, nums):      # 排序法【时间复杂度O(nlgn)，空间复杂度O(1)或O(n)】
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
