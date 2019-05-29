"""最大最小之差
小Q的好朋友牛牛在纸上写了长度为n的正整数数列。
牛牛要求小Q每次从数列中选取两个数a,b，把这两个数从数列中移除出去，然后在数列中加入a * b + 1，直到只剩一个数为止。
小Q发现根据操作顺序的不同，最后得到的数的大小也不一样。
小Q现在想让你帮他计算，在所有情况中能获得的最大值减去能获得的最小值等于多少？
输入描述
第一行一个正整数n(1 <= n <= 50)，表示正整数序列的长度；
在接下来的n行中，每行输入一个正整数ai，即初始数列中的每一个数。保证所有数据计算结果均在64位有符号整数范围内。
输出描述
输出一个数，表示最大最小之差。
示例1
输入
3
1
2
3
输出
2
"""


def func(n, arr):
    arr.sort()
    arr1, arr2 = arr[:], arr[:]
    for i in range(n-1):
        a1 = arr1.pop()
        b1 = arr1.pop()
        arr1.append(a1*b1+1)
        arr1.sort()
        a2 = arr2.pop(0)
        b2 = arr2.pop(0)
        arr2.append(a2*b2+1)
        arr2.sort()
    return arr2[0]-arr1[0]


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
print(func(n, arr))
