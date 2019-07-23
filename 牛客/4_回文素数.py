"""题目描述
如果一个整数只能被1和自己整除,就称这个数是素数。               【1不是素数(素数)】
如果一个数正着反着都是一样,就称为这个数是回文数。例如:6, 66, 606, 6666
如果一个数字既是素数也是回文数,就称这个数是回文素数
牛牛现在给定一个区间[L, R],希望你能求出在这个区间内有多少个回文素数。
输入描述:
输入包括一行,一行中有两个整数(1 ≤ L ≤ R ≤ 1000)
输出描述:
输出一个整数,表示区间内回文素数个数。
示例1
输入
复制
100 150
输出
复制
2
"""

"如果一个整数只能被1和自己整除,就称这个数是素数。【1不是素数(素数)】"
"如果一个数正着反着都是一样,就称为这个数是回文数。例如:6, 66, 606, 6666"
"素数（质数）：2 3 5 7 11 13 17 19 23...."         "合数"


import math
L, R = map(int, input().split())
count = 0
L = max(2, L)                                       # 注意边界【1不是素数，可以从2开始】
for i in range(L, R+1):
    flag = True                                     # 定义一个【布尔值】
    for j in range(2, int(math.sqrt(i))+1):         # 注意【int(math.sqrt(i))+1】
        if i % j == 0:
            flag = False
            break                                   # break 是跳出本轮循环，还会要执行 回文检验，所以用flag判断一下
    if flag:
        if str(i)[::-1] == str(i):
            count += 1
print(count)


def isf(s):
    if str(s) != str(s)[::-1]:
        return False
    if s <= 1:
        return False
    for i in range(2, int(math.sqrt(s))+1):
        if s % i == 0:
            return False
    return True


num = 0
L, R = map(int, input().split())
print(len(list(filter(lambda c: isf(c), range(L, R + 1)))))
