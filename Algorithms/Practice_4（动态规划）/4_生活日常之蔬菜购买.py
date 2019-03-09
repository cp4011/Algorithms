'''生活日常之蔬菜购买
Description
Rahul wanted to purchase vegetables mainly brinjal, carrot and tomato. There are N different vegetable sellers in a line
Each vegetable seller sells all three vegetable items, but at different prices. Rahul, obsessed by his nature to spend
optimally, decided not to purchase same vegetable from adjacent shops. Also, Rahul will purchase exactly one type of
vegetable item (only 1 kg) from one shop. Rahul wishes to spend minimum money buying vegetables using this strategy.
Help Rahul determine the minimum money he will spend.
Input
First line indicates number of test cases T. Each test case in its first line contains N denoting the number of
vegetable sellers in Vegetable Market. Then each of next N lines contains three space separated integers denoting
cost of brinjal, carrot and tomato per kg with that particular vegetable seller.
Output
For each test case, output the minimum cost of shopping taking the mentioned conditions into account in a separate line.
Constraints:1 <= T <= 101 <= N <= 100000 Cost of each vegetable(brinjal/carrot/tomato) per kg does not exceed 10^4
Sample Input 1
1
3
1 50 50
50 50 50
1 50 50
Sample Output 1
52
'''


# 动态规划
def find_optimal_purchase(sellers):
    dp = [[0, 0, 0] for _ in range(len(sellers) + 1)]

    for i, seller in enumerate(sellers, 1):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + seller[0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + seller[1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + seller[2]

    return min(dp[len(sellers)])


num_case = int(input())
for _ in range(num_case):
    n = int(input())
    array = []
    for i in range(n):
        array.append([int(i) for i in input().strip().split()])
    result = find_optimal_purchase(array)
    print(result)









