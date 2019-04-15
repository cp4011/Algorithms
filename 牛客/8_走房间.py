"""题目描述
存在n+1个房间，每个房间依次为房间1 2 3...i，每个房间都存在一个传送门，i房间的传送门可以把人传送到房间pi(1<=pi<=i),
现在路人甲从房间1开始出发(当前房间1即第一次访问)，每次移动他有两种移动策略：
    A. 如果访问过当前房间 i 偶数次，那么下一次移动到房间i+1；
    B. 如果访问过当前房间 i 奇数次，那么移动到房间pi；
现在路人甲想知道移动到房间n+1一共需要多少次移动；
输入描述:
第一行包括一个数字n(30%数据1<=n<=100，100%数据 1<=n<=1000)，表示房间的数量，接下来一行存在n个数字 pi(1<=pi<=i), pi表示
从房间i可以传送到房间pi。
输出描述:
输出一行数字，表示最终移动的次数，最终结果需要对1000000007 (10e9 + 7) 取模。
示例1
输入
2
1 2
输出
4
说明
开始从房间1 只访问一次所以只能跳到p1即 房间1， 之后采用策略A跳到房间2，房间2这时访问了一次因此采用策略B跳到房间2，之后
采用策略A跳到房间3，因此到达房间3需要 4 步操作。
"""


# 1
n = int(input())
pi = list(map(int, input().split()))
res = []                                            # res[i] 存储 i房间走到下一个房间i+1的步数
for i in range(n):
    if pi[i] == i+1:
        res.append(2)
    else:
        res.append(sum(res[pi[i]-1:i])+2)           # res = [2,(2) + 2,....]
print(sum(res) % 1000000007)


# 2
def main():
    n = int(input())
    pi = list(map(int, input().split()))
    dp = [0]                                        # dp[i] 存储的是从房间1（下标为0），走到i房间需要的步数
    for i in range(1, n + 1):
        dp.append(0)                                # 从房间1走到房间i-1的步数dp[i - 1] + 折返回到房间pi[i - 1]并重新到房间i-1的步数 + 2
        dp[i] = 2 * dp[i - 1] - dp[pi[i - 1] - 1] + 2
    print(dp[n] % 1000000007)


if __name__ == '__main__':
    main()


# 3
try:
    while True:
        x = input()
        if x == '':
            break
        n = int(x)
        l = [int(e)-1 for e in input().split()]     # - 1 后，房间数i 就是下标i
        s = []
        for e in l:
            t = (2+sum(s[e:])) % 1000000007
            s.append(t)
        print(sum(s) % 1000000007)
except:
    pass