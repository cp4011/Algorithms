"""给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。
滑动窗口每次只向右移动一位。      返回滑动窗口最大值。
示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
注意：
你可以假设 k 总是有效的，1 ≤ k ≤ 输入数组的大小，且输入数组不为空。
进阶：     你能在线性时间复杂度内解决此题吗？
"""


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':     # DP【时间复杂度O(N)，对长度为N的数组处理了3次。空间复杂度O(N)]
        """ 从左到右遍历数组，建立数组 left，其中 left[j] 是从块的开始到下标 j 最大的元素，方向 左->右
            从右到左遍历数组，建立数组 right，right[j] 是从块的结尾到下标 j 最大的元素，方向 右->左
            开头元素为 i ，结尾元素为j的滑动窗口，right[i] 是左侧块内的最大元素，left[j] 是右侧块内的最大元素。滑动窗口中的最大元素为 max(right[i], left[j])。
            建立输出数组 max(right[i], left[i + k - 1])，其中 i 取值范围为 (0, n - k + 1)。"""
        n = len(nums)               # [1,3,-1,  -3,5,3, 6,7]    若k=3（以k划分块
        if n * k == 0:
            return []
        if k == 1:
            return nums
        left = [0] * n              # [1,3,3,   -3,5,5, 6,7]    left[i] 是从块的开始到下标 i 最大的元素，方向 左->右
        left[0] = nums[0]
        right = [0] * n             # [3,3,-1,  5,5,3,  7,7]    right[j] 是从块的结尾到下标 j 最大的元素，方向 右->左
        right[n - 1] = nums[n - 1]
        for i in range(1, n):       # 从左往右  【从元素第一位即索引0开始，k个元素为一块划分】
            if i % k == 0:          # 块 开始（直接将当前遍历的最大值置位块开始元素）
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            j = n - i - 1           # 从右往左
            if (j + 1) % k == 0:
                right[j] = nums[j]  # 块 结束（从右到左）
            else:
                right[j] = max(right[j + 1], nums[j])
        output = []
        for i in range(n - k + 1):                          # 若n=8,k=3
            output.append(max(left[i + k - 1], right[i]))   # left数组遍历索引2到7，right数组遍历0到6，最后输出output只有7个（N-k+1）滑动窗口的最大值
        return output

