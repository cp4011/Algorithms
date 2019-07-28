"""给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:
输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""


class Solution:
    def maxProfit(self, prices):    # 可参与多笔交易，卖出股票后，无法在第二天买入股票 (即冷冻期为 1 天)
        """ 1. 如果我们index:i天为冷冻期，那么只能说明index:i-1天卖掉了股票，那么i天的收益和i-1天是一样的
                    cooldown[i]=sell[i-1]
            2. 如果我们考虑index:i天卖出，要求利润最大的话。一种情况是index:i-1当天买入了股票，另一种情况是index:i-1
            之前就持有股票，  index:i-1天也可以卖出，那么我们就需要考虑index:i-1卖出更好呢？还是index:i卖出更好呢？
                    sell[i]=max(sell[i-1], buy[i-1]+prices[i])
            3. 如果我们考虑index:i天买入，要求利润最大的话。一种情况是index:i-1天是冷冻期，另一种情况是index:i-1天
            不是冷冻期，也就是index:i-1天也可以买入，那么我们就需要考虑index:i-1买入更好呢？还是index:i买入更好呢？
                    buy[i]=max(buy[i-1], cooldown[i-1]-prices[i])
            我们第一天不可能卖出或者冻结，那么这两个sell[0]=0 cooldown[0]=0，但是我们第一天可以买入啊，
            所以buy[0]=-prices[0]。还有一点要注意的就是，我们一定是最后一天卖出或者最后一天冻结利润最大。"""
        if not prices:
            return 0
        len_prices = len(prices)
        buy, sell, cooldown = [0]*len_prices, [0]*len_prices, [0]*len_prices
        buy[0] = -prices[0]
        for i in range(1, len_prices):
            cooldown[i] = sell[i-1]
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i])

        return max(sell[len_prices - 1], cooldown[len_prices - 1])

    def maxProfit1(self, prices):
        """sell[i]表示截至第i天，最后一个操作是卖时的最大收益；buy[i]表示截至第i天，最后一个操作是买时的最大收益；
        cool[i]表示截至第i天，最后一个操作是冷冻期时的最大收益；
        递推公式：
        sell[i] = max(buy[i-1]+prices[i], sell[i-1]) (第一项表示第i天卖出，第二项表示第i天冷冻)
        buy[i] = max(cool[i-1]-prices[i], buy[i-1]) （第一项表示第i天买进，第二项表示第i天冷冻）
        cool[i] = max(sell[i-1], buy[i-1], cool[i-1])"""
        n = len(prices)
        if n == 0:
            return 0
        sell = [0 for _ in range(n)]
        buy = [0 for _ in range(n)]
        cool = [0 for _ in range(n)]
        buy[0] = -prices[0]
        for i in range(1, n):
            sell[i] = max(buy[i-1] + prices[i], sell[i-1])
            buy[i] = max(cool[i-1] - prices[i], buy[i-1])
            cool[i] = max(sell[i-1], buy[i-1], cool[i-1])
        return sell[-1]
