"""简单选择排序(Select Sort)
1. 初始状态：无序区为R[1..n]，有序区为空；
2. 第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无序区中-选出关键字最小
的记录 R[k]，将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
3. n-1趟结束，数组有序化了。

简单选择排序同样对数据操作n-1轮，每轮找出一个最大（小）值。
操作指选择，即未排序数逐个比较交换，争夺最值位置，每轮将一个未排序位置上的数交换成已排序数，即每轮选一个最值。
每轮操作O(n)次，共O（n）轮，                   时间复杂度O(n^2)。
额外空间开销出在交换数据时那一个过渡空间，    空间复杂度O(1)。
"""


def SelectSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(0, n - 1):
        minIndex = i
        for j in range(i + 1, n):       # 比较一遍，记录索引不交换
            if lst[j] < lst[minIndex]:
                minIndex = j
        if minIndex != i:               # 按索引交换
            (lst[minIndex], lst[i]) = (lst[i], lst[minIndex])
    return lst


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = SelectSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
