"""希尔排序(Shell Sort)
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：
1. 选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
2. 按增量序列个数k，对序列进行k 趟排序；
3. 每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，
整个序列作为一个表来处理，表长度即为整个序列的长度。

希尔排序是插入排序的高效实现（大家可以比对一下插入排序和希尔排序的代码），对简单插入排序减少移动次数优化而来。
简单插入排序每次插入都要移动大量数据，前后插入时的许多移动都是重复操作，若一步到位移动效率会高很多。
若序列基本有序，简单插入排序不必做很多移动操作，效率很高。
希尔排序将序列按固定间隔划分为多个子序列，在子序列中简单插入排序，先做远距离移动使序列基本有序；逐渐缩小间隔重复操作，
    最后间隔为1时即简单插入排序。
希尔排序对序列划分O(n)次，每次简单插入排序O(logn)，时间复杂度O(nlogn)
额外空间开销出在插入过程数据移动需要的一个暂存，空间复杂度O(1)

希尔排序的核心在于间隔序列的设定。既可以提前设定好间隔序列，也可以动态的定义间隔序列
"""


def ShellSort(lst):
    def shellinsert(arr, d):
        n = len(arr)
        for i in range(d, n):
            j = i - d
            temp = arr[i]  # 记录要出入的数
            while j >= 0 and arr[j] > temp:  # 从后向前，找打比其小的数的位置
                arr[j + d] = arr[j]  # 向后挪动
                j -= d
            if j != i - d:
                arr[j + d] = temp

    n = len(lst)
    if n <= 1:
        return lst
    d = n // 2
    while d >= 1:
        shellinsert(lst, d)
        d = d // 2
    return lst


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = ShellSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
