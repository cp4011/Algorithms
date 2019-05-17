"""小明家有一些彩球，一段时间后小明玩耍时将它们无序的散落在家中，一天，小明想对其进行整理，规则为一个篮子中只放一种颜色彩球，
可有多个篮子放同一颜色的球，每个篮子里的球不少于2个。假设小明整理好后，能使各篮子中彩球数量是相同的，则认为小明整理好了。
用一个数字表示一种颜色彩球，一组数表示小明已经找到了的彩球，问小明用找到的全部彩球能按规则整理好么？
输入
第一行彩球总数: n,  2<n<10000
第二行一段整数ai,  1<ai<10000  (排除ai全部相等的情况)
输出
若能整理好，最小篮子数；否则0

样例输入
6
1 1 2 2 2 2
样例输出
3
提示
样例输入:
6
1 1 2 2 2 2
样例输出:
3      	tip: [1, 1] [2, 2] [2, 2]
样例输入:
5
1 1 1 2 2
样例输出:
0     		tip: [1 1 1] [2 2]

样例输入:
6
1 1 1 2 2 2
样例输出:
2      	tip: [1 1 1] [2 2 2]
"""


'''最大公约数：指两个或多个整数共有约数中最大的一个
最小公倍数：两个或多个整数公有的倍数叫做它们的公倍数，其中除0以外最小的一个公倍数就叫做这几个整数的最小公倍数
二者关系：两个数之积=最小公倍数*最大公约数
'''


# 两数最大公约数
def func(m, n):
    return m if n == 0 else func(n, m%n)

# h = func(m, n)
# 两数最小公倍数
def gongbei(m, n, h):
    return m*n/h


# 思路：最大公约数
def cal(n, l):
    result = 0
    for r in range(min(l), 2-1, -1):
        flag = True
        for v in l:
            if v % r != 0:
                flag = False
                break
        if flag == True:
            result = r
            return int(n / result)
    return result


if __name__ == '__main__':
    n = 10
    ball = [1, 1, 2, 2, 2, 2, 3, 4, 3, 4]
    dict_color = {}                         # 字典记数
    for b in ball:
        dict_color[b] = dict_color.get(b, 0) + 1
    print(cal(n, dict_color.values()))
