"""小明在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:   输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
"""

'''双指针技术，就是相当于有一个窗口，两个窗口都是从左边出发,窗口的左右两边就是两个指针，我们根据窗口内值之和来确定窗口的位置和宽度。
由于是连续的，差为1的一个序列，那么求和公式是(a0+an)*n/2
    1. //相等，那么就将窗口范围的所有数添加进结果集
    2. //如果当前窗口内的值之和小于sum，那么右边窗口右移一下
    3. //如果当前窗口内的值之和大于sum，那么左边窗口右移一下
'''


class Solution:
    def FindContinuousSequence(self, tsum):
        head = 1
        last = 2
        sum = 3
        r = []
        while last <= (tsum+1)/2:
            if sum == tsum:                 # 当前窗口内的值之和与tsun相等，那么就将窗口范围的所有数添加进结果集
                r.append(range(head, last+1))
                last = last + 1
                sum = sum + last
            elif sum < tsum:                # 当前窗口内的值之和小于sum，那么右边窗口右移一下
                last = last + 1
                sum = sum + last
            else:
                sum = sum - head            # 当前窗口内的值之和大于sum，那么左边窗口右移一下
                head = head + 1
        return r


# 暴力法
class Solution2:
    def FindContinuousSequence(self, tsum):
        res = []
        for i in range(1, tsum/2+1):            # i<j
            for j in range(i, tsum/2+2):
                tmp = (j+i)*(j-i+1)/2           # 公差为1的求和
                if tmp > tsum:
                    break
                elif tmp == tsum:
                    res.append(range(i, j+1))
        return res

        res = []
        for i in range(1, tsum // 2 + 2):       # i>j
            for j in range(1, i):
                s = (i + j) * (i - j + 1) / 2
                if s < tsum:
                    break
                elif s == tsum:
                    res.append(range(j, i + 1))
        return res
