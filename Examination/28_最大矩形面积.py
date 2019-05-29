"""给定一组非负整数组成的数组h，代表一组柱状图的高度，其中每个柱子的宽度都为1。 在这组柱状图中找到能组成的最大矩形的面积
（如图所示）。 入参h为一个整型数组，代表每个柱子的高度，返回面积的值。

输入描述:
输入包括两行,第一行包含一个整数n(1 ≤ n ≤ 10000)
第二行包括n个整数,表示h数组中的每个值,h_i(1 ≤ h_i ≤ 1,000,000)
输出描述:
输出一个整数,表示最大的矩阵面积。

输入例子1:
6
2 1 5 6 2 3
输出例子1:
10
"""
'''遍历数组每一个值，然后用两个指针从当前位置向两边寻找左右边界，大于等于当前值时则对应指针加1，
 这样最后得到以当前值为最小高度的矩形宽度，然后计算面积并与最大值比较并保存其中最大的值'''


def func(arr, n):
    ans = [0] * n
    for i in range(n):
        count = 1
        j = i - 1
        while j >= 0 and arr[i] <= arr[j]:
            j -= 1
            count += 1
        k = i + 1
        while k < n and arr[i] <= arr[k]:
            k += 1
            count += 1
        ans[i] = arr[i] * count
    return max(ans)


n = int(input())
arr = [int(i) for i in input().split()]
print(func(arr, n))
