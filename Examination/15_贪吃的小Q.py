"""小Q的父母要出差N天，走之前给小Q留下了M块巧克力。小Q决定每天吃的巧克力数量不少于前一天吃的一半，但是他又不想在父母回来之前的某一天没有巧克力吃，请问他第一天最多能吃多少块巧克力

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，表示父母出差的天数N(N<=50000)和巧克力的数量M(N<=M<=100000)。

输出描述:
输出一个数表示小Q第一天最多能吃多少块巧克力。

输入例子1:
3 7

输出例子1:
4
"""

N, M = map(int, input().split())     # M块巧克力，小Q每天吃的巧克力数量不少于前一天吃的一半，第一天最多能吃多少块巧克力


def my_sum(s):
    import math
    total_sum = 0
    for i in range(N):
        total_sum += s
        s = math.ceil(s / 2)        # math.ceil()
    return total_sum


low, high = 1, M
while low <= high:
    mid = (low + high) // 2         # 第一天最多能吃多少块巧克力，那以后最多吃前一天的一半就能得到第一天最多能吃的块数了
    if my_sum(mid) == M:            # 刚好相等，打印出第一天最多能吃的巧克力块数是：mid
        print(mid)
        break
    elif my_sum(mid) < M:
        low = mid + 1
    else:
        high = mid - 1
if low > high:                      # 判断循环是否有break结束，二分查找过程中，没有整数mid能使得满足刚好等于M
    print(low - 1)


# 超时 10%
def func(n, m):
    """此题与13题（跳跃问题）有点区别，此题 恰好 =M 时 可以直接弹出，没有存在恰好的情况，就输出弹出while时条件： low-1"""
    def solve(first):
        ans = first
        for i in range(n-1):
            first = first * 0.5
            if first < 1:
                return False
            ans += first
        return ans > m
    l, r = 1, m
    while l < r:
        mid = (l+r) // 2
        if solve(mid):
            r = mid - 1
        else:
            l = mid
    return l


n, m = (int(i) for i in input().split())
print(int(func(n, m)))
