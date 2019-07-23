"""给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 【两笔】 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。"""


def maxProfit(prices):            # 最多只能两次买卖股票（两次遍历, 时间O(n)，空间O(n)）
    if not prices:                  # prices输入 [3,3,5,0,0,3,1,4]
        return 0

    profits = []
    max_profit = 0                  # [0,0,2,2,2,3,3,4]
    current_min = prices[0]
    for price in prices:                        # 正向遍历（第一次买卖）
        current_min = min(current_min, price)   # 记录当前遍历到的最小值（第一次买入的最小价格）
        max_profit = max(max_profit, price - current_min)   # 当前价格 减去 已经遍历到的最小买入价格（第一次买卖）
        profits.append(max_profit)                          # 存入数组

    total_max = 0
    max_profit = 0
    current_max = prices[-1]
    for i in range(len(prices) - 1, -1, -1):                # 反向遍历（第二次买卖）
        current_max = max(current_max, prices[i])           # 记录反向遍历到的最大值（第二次卖出的价格）
        max_profit = max(max_profit, current_max - prices[i])   # 当前价格 减去已经遍历到的最大卖出价格（第二次买卖）
        total_max = max(total_max, max_profit + profits[i])     # 遍历：取两次买卖相加的最大值
    return total_max


print(maxProfit([3,3,5,0,0,3,1,4]))
