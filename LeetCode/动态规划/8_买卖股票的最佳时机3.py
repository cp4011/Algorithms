"""给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
"""

'''leftMaxProfit[i] + leftMaxProfit[i] 之和最大值
    # 要买两笔 我们可以一笔从数组的左边开始搜索最优利润，第二笔从数组右边开始搜索最优解 然后合并两个数组的最优解
    #  left[i] 代表 第一笔第i天以前得到的最大利润 转换成方程 left[i]=max(left[i-1],prices[i]-min)    min:最小买入价
    #  right[i] 代表 第二笔第i天以后得到的最大利润 转换成方程 right[i]=max(right[i+1],max-prices[i]) max:最大卖出价
'''
class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:                              # 注意为空
            return 0
        length = len(prices)
        dp_left = [0] * length
        m_min = prices[0]
        for i in range(length):                     # 正向遍历（第一笔交易）
            m_min = min(m_min, prices[i])           # 记录正向遍历到i时的当前最小值
            dp_left[i] = max(prices[i] - m_min, dp_left[i-1])

        dp_right = [0] * length
        m_max = prices[-1]
        for i in range(length-1, -1, -1):           # 反向遍历（第二笔交易）
            m_max = max(m_max, prices[i])           # 记录反向遍历到i时的当前最大值
            dp_right[i] = max(m_max - prices[i], dp_right[i-1])

        total_max = 0
        for i in range(length):
            total_max = max(total_max, dp_left[i] + dp_right[i])
        return total_max


class Solution(object):
    def maxProfit(self, p):
        if not p:
            return 0
        sell, buyd, n, minp, maxp = [0], [0], len(p), p[0], p[-1]
        for i in range(1, n):
            minp, maxp = min(minp, p[i]), max(maxp, p[n-i-1])
            sell.append(max(sell[i-1], p[i] - minp))
            buyd.append(max(buyd[i-1], maxp - p[n-i-1]))
        return max(sell[i] + buyd[n-i-1] for i in range(n))


