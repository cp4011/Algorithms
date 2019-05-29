def permutations(m, n):
    """排列的个数"""            # 如 C(7,3)
    res = 1
    for i in range(1, n+1):     # 共n个数相乘，i 取 1 2 3。也可是range(n),从1开始，为了和下面组合的个数统一
        res *= (m-i+1)          # (m+1-i)取 7 6 5
    return res


def combination(m, n):
    """组合的个数"""            # 如 C(7,3)
    res = 1
    for i in range(1, n+1):     # i 取 1 2 3
        res *= (m-i+1)          # (m+1-i)取 7 6 5
        res //= i               # 必须是 整除//
    return res


print(permutations(7, 3), combination(7, 3))
