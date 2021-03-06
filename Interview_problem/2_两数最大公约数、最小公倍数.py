'''最大公约数：指两个或多个整数共有约数中最大的一个
最小公倍数：两个或多个整数公有的倍数叫做它们的公倍数，其中除0以外最小的一个公倍数就叫做这几个整数的最小公倍数
二者关系：两个数之积=最小公倍数*最大公约数'''


def func(m, n):
    """两数最大公约数"""
    return m if n == 0 else func(n, m % n)

# h = func(m, n)


def gongbei(m, n, h):
    """两数最小公倍数"""
    return m*n/h
