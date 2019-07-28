""" 基数排序（Radix Sort）
1. 取得数组中的最大数，并取得位数；
2. arr为原始数组，从最低位开始取每个位组成radix数组；
3. 对radix进行计数排序（利用计数排序适用于小范围数的特点）；

基数排序基于分别排序，分别收集，所以是稳定的。但基数排序的性能比桶排序要略差，每一次关键字的桶分配都需要O(n)的时间复杂度，
而且分配之后得到新的关键字序列又需要O(n)的时间复杂度。假如待排数据可以分为d个关键字，则基数排序的时间复杂度将是O(d*2n) ，
当然d要远远小于n，因此基本上还是线性级别的。
基数排序的空间复杂度为O(n+k)，其中k为桶的数量。一般来说n>>k，因此额外空间需要大概n个左右
"""


import math
def RadixSort(lst):
    def getbit(x, i):  # 返回x的第i位（从右向左，个位为0）数值
        y = x // pow(10, i)
        z = y % 10
        return z

    def CountSort(lst):
        n = len(lst)
        num = max(lst)
        count = [0] * (num + 1)
        for i in range(0, n):
            count[lst[i]] += 1
        arr = []
        for i in range(0, num + 1):
            for j in range(0, count[i]):
                arr.append(i)
        return arr

    Max = max(lst)
    for k in range(0, int(math.log10(Max)) + 1):  # 对k位数排k次,每次按某一位来排
        arr = [[] for i in range(0, 10)]
        for i in lst:  # 将ls（待排数列）中每个数按某一位分类（0-9共10类）存到arr[][]二维数组（列表）中
            arr[getbit(i, k)].append(i)
        for i in range(0, 10):  # 对arr[]中每一类（一个列表）  按计数排序排好
            if len(arr[i]) > 0:
                arr[i] = CountSort(arr[i])
        j = 9
        n = len(lst)
        for i in range(0, n):  # 顺序输出arr[][]中数到ls中，即按第k位排好
            while len(arr[j]) == 0:
                j -= 1
            else:
                lst[n - 1 - i] = arr[j].pop()
    return lst


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = RadixSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
