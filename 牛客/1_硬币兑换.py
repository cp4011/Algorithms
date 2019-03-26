"""A 国一共发行了几种不同面值的硬币，分别是面值 1 元，2 元，5 元，10 元，20 元，50 元， 100 元。假设每种面值的硬币数量
是无限的，现在你想用这些硬币凑出总面值为 n 的硬币， 同时你想让选出的硬币中，不同的面值种类尽可能多;在面值种类尽可能多的
情况下，你想 让选择的硬币总数目尽可能多，请问应该怎么选择硬币呢?
输入描述:
第一行包含一个数字𝑛，表示要凑出的面值。1 ≤ 𝑛 ≤ 109
输出描述:
输出两个整数，分别表示最多能有多少种类型的硬币以及在类型最多的情况下最多能用上多少枚硬币。
示例1
输入
3
输出
2 2
示例2
输入
10
输出
3 5
"""


n = int(input())
arr = [1, 2, 5, 10, 20, 50, 100]
type_count = 0
for i in arr:                   # 从小到大遍历
    if n >= i:
        n -= i
        type_count += 1
    else:
        break
print(type_count, type_count + n)
