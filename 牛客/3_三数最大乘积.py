"""题目描述
给定一个无序数组，包含正数、负数和0，要求从中找出3个数的乘积，使得乘积最大，要求时间复杂度：O(n)，空间复杂度：O(1)
输入描述:
无序整数数组A[n]
输出描述:
满足条件的最大乘积
示例1
输入
复制
3 4 1 2
输出
复制
24
"""


a = int(input())
num = list(map(int, input().strip().split()))
num.sort()
b = num[-1]*num[-2]*num[-3]
c = num[-1]*num[0]*num[1]
print(max(b, c))


def max_l(l,n):
    if n < 3:
        return None
    if n == 3:
        return l[0]*l[1]*l[2]
    a, b = [], []
    a1, a2 = l[:], l[:]
    for i in range(3):
        max1 = max(a1)
        a.append(max1)
        a1.remove(max1)
    for i in range(2):
        min2 = min(a2)
        b.append(min2)
        a2.remove(min2)
    maxNum = max(a[0]*a[1]*a[2], b[0]*b[1]*a[0])
    return maxNum


n = int(input().strip())
l = list(map(int, input().strip().split()))
print(max_l(l, n))
