"""给出一个区间的集合，请合并所有重叠的区间。
示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
'''先按首位置进行排序;接下来,如何判断两个区间是否重叠呢?比如a = [1,4],b = [2,3]
当a[1] >= b[0]说明两个区间有重叠.左边位置一定是a[0],而右边位置是max(a[1], b[1]),所以,我们就能找出整个区间为:[1,4]'''


class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals)       # 排序
        i, n = 0, len(intervals)
        ans = []
        while i < n:        # 外层循环
            left, right = intervals[i][0], intervals[i][1]
            while i+1 < n and intervals[i+1][0] <= right:   # 循环：处理里面重叠的区间
                right = max(right, intervals[i+1][1])       # 嵌套区间中的right
                i += 1
            ans.append([left, right])
            i += 1              # 注意此处要 i += 1
        return ans

