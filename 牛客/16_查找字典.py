"""小易在学校中学习了关于字符串的理论, 于是他基于此完成了一个字典的项目。
小易的这个字典很奇特, 字典内的每个单词都包含n个'a'和m个'z', 并且所有单词按照字典序排列。
小易现在希望你能帮他找出第k个单词是什么。

输入描述:
输入包括一行三个整数n, m, k(1 <= n, m <= 100, 1 <= k <= 109), 以空格分割。

输出描述:
输出第k个字典中的字符串，如果无解，输出-1。
示例1
输入
2 2 6
输出
zzaa
说明
字典中的字符串依次为aazz azaz azza zaaz zaza zzaa
"""
'''排列组合，n个'a'和m个'z'，只能组成$C_{n+m}^n$，记为count(n+m,n) 个单词。  【如n+m个位置，选n个位置来放a，另外m个b位置已经确定】
思路：
假设第一个字符为a，则剩下n-1个'a'和m个'z'组成的子序列只能构成count(n-1+m,n-1)个单词，且是字典中前count(n-1+m,n-1)个单词。
比较k和count(n-1+m,n-1)，若k小，说明k是前count(n-1+m,n-1)个单词，则第一个字符必为'a'。子问题化为在子序列(n-1个'a'和m个'z')找到第k个单词
若k大，则说明第一个字符必为'z',单词是以'z'开头的单词中的第k-count(n-1+m,n-1)个。子问题化为在子序列(n个'a'和m-1个'z')找到第k-count(n+m-1,m-1)个单词。
eg:n=2,m=2,k=5
假设第一个字符为a,则剩下1个a,2个z只能构成3个单词，且是字典中前3个单词(aamm,amam,amma)
k>3，则第一个字符必为z。原问题化为在n=2,m=1,k=2，即在剩下2个a，1个z中找到第2个单词
'''


def Cnm(n, m):
    a, b = 1, 1
    for i in range(n+1, n+m+1):   # 注意从n+1开始的，因为前面除于了n的阶乘
        a *= i
    for i in range(1, m+1):
        b *= i
        # ans //= i               # 必须是 //，要不然会溢出报错【a=10, b=21 b/a 输出结果 2.1】
    return a / b


n, m, k = map(int, input().strip().split())
if k > Cnm(n, m):
    print(-1)
else:
    ans = ""
    while n > 0 and m > 0:
        temp = Cnm(n-1, m)
        if k > temp:
            k -= temp           # 注意要减去temp
            ans += "z"
            m -= 1
        else:
            ans += "a"
            n -= 1
    ans += "a" * n
    ans += "z" * m
    print(ans)
