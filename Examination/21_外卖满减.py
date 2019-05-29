"""你打开了美了么外卖，选择了一家店，你手里有一张满X元减10元的券，店里总共有n种菜，第i种菜一份需要A_i元，因为你不想吃
太多份同一种菜，所以每种菜你最多只能点一份，现在问你最少需要选择多少元的商品才能使用这张券。

输入描述:
第一行两个正整数n和X，分别表示菜品数量和券的最低使用价格。（1≤n≤100, 1≤X≤10000） 接下来一行n个整数，
第i个整数表示第i种菜品的价格。（1≤A_i≤100）
输出描述:
一个数，表示最少需要选择多少元的菜才能使用这张满X元减10元的券，保证有解。

输入例子1:
5 20
18 19 17 6 7
输出例子1:
23
"""


def func(arr):
    if not arr:
        return
    a = min(arr)
    count = 0
    count += a
    for i in range(len(arr)):
        arr[i] -= a
    while arr.count(0) != n:
        index = arr.index(0)
        func(arr[:index])
        func(arr[index + 1:])
    return count


n = int(input())
arr = [int(i) for i in input().split()]
print(func(arr))

