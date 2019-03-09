'''实现Shell排序
Description
实现Shell排序，对给定的无序数组，按照给定的间隔变化（间隔大小即同组数字index的差），打印排序结果，注意不一定是最终排序结果！
Input
输入第一行表示测试用例个数，后面为测试用例，每一个用例有两行，第一行为给定数组，第二行为指定间隔，每一个间隔用空格隔开。
Output
输出的每一行为一个用例对应的指定排序结果。
Sample Input 1
1
49 38 65 97 76 13 27 49 55 4
5 3
Sample Output 1
13 4 49 38 27 49 55 65 97 76
'''


# 希尔排序
def shell_sort(array):
    n = len(array)
    gap = round(n/2)       # 初始步长,用round四舍五入取整
    while gap > 0:
        for i in range(gap, n):        # 每一列进行插入排序,从gap 到 n-1
            temp = array[i]            # 记住要插入的这个数
            j = i
            while ( j >= gap and array[j-gap] > temp ):    # 直接插入排序（前面的数大于要插入的tmep）
                array[j] = array[j-gap]        # 将前面较大的这个数赋值到后面
                j = j - gap
            array[j] = temp
        gap = round(gap/2)                     # 重新设置步长
    return array
print(shell_sort([3, 2,8, 6,4,10]))


# def shell_sort_gap(array, gaps):
#     n = len(array)
#     for gap in gaps:
#         for i in range(gap, n):
#             temp = array[i]
#             j = i
#             while(j >= gap and array[j-gap] > temp):
#                 array[j] = array[j-gap]
#                 j = j-gap
#             array[j] = temp
#     return array
#
#
# T = int(input())
# for i in range(T):
#     array = [int(i) for i in input().split()]
#     gaps = [int(i) for i in input().split()]
#     result = shell_sort_gap(array, gaps)
#     for i in range(len(result)):
#         if i == len(result) - 1:
#             print(result[i])
#         else:
#             print(result[i], end=' ')
