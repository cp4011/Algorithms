"""小Q有X首长度为A的不同的歌和Y首长度为B的不同的歌，现在小Q想用这些歌组成一个总长度正好为K的歌单，每首歌最多只能在歌单中
出现一次，在不考虑歌单内歌曲的先后顺序的情况下，请问有多少种组成歌单的方法。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个整数，表示歌单的总长度K(1<=K<=1000)。
接下来的一行包含四个正整数，分别表示歌的第一种长度A(A<=10)和数量X(X<=100)以及歌的第二种长度B(B<=10)和数量Y(Y<=100)。保证A不等于B。

输出描述:
输出一个整数,表示组成歌单的方法取模。因为答案可能会很大,输出对1000000007取模的结果。

输入例子1:
5
2 3 3 3

输出例子1:
9
"""
'''要组成总长度为K的歌单（有X首长度为A的不同的歌和Y首长度为B的不同的歌，每首歌最多只能在歌单中
出现一次，不考虑顺序），如果从X个A中取出i个A之后的差刚好能够除以B，并且（K-A*i）/B结果小于B的个数Y的话，那么就可以取。
    结果的个数为：组合C(X,i)*C(Y,（K-A*i）/B)'''

K = int(input())
A, X, B, Y = map(int, input().split())
maxA = min(K // A, X)                   # 长为k的歌单中最多需要长度为A的不同歌多少首，与长为A的歌总共有X首 中去较小者
choice = []
for i in range(maxA+1):
    if (K-i*A) % B == 0:                # 对于K，如果从X个A中取出i个A之后的差刚好能够除以B
        tmp = (K-i*A) // B
        if tmp <= Y:                    # 且（K-A*i）/B结果 小于等于 B的个数Y
            choice.append([i, tmp])


def combination(m,n):           # 组合的个数 C(m,n)
    res = 1
    for i in range(1, n+1):
        res *= (m+1-i)
        res //= i               # 必须要有 整除//
    return res

res = 0
for cho in choice:
    res += (combination(X, cho[0]))*(combination(Y, cho[1]))
print(res % 1000000007)         # 记住要 %



'''case通过率为80.00%
用例:
100
1 100 2 100
对应输出应该为:480218926
你的输出为:941226889
'''
def func(a, x, b, y, k):
    def num_comb(p, q):
        s1, s2 = 1, 1
        for i in range(p-q+1, p+1):
            s1 *= i
        for j in range(1, q+1):
            s2 *= j
        return s1 // s2
    l1, l2 = [], []
    temp = []
    for i in range(1, x+1):
        l1.append(a*i)
    for j in range(1, y+1):
        l2.append(b*j)
    for i in l1:
        for j in l2:
            if i+j == k:
                temp.append([i, j])
    ans = 0
    for i in temp:
        n = i[0] // a
        m = i[1] // b
        ans += num_comb(x, n) * num_comb(y, m)
    return ans % 1000000007


k = int(input())
a, x, b, y = [int(i) for i in input().split()]
print(func(a, x, b, y, k))

