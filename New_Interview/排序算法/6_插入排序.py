""" 简单插入排序(Insert Sort)
1. 从第一个元素开始，该元素可以认为已经被排序；
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描；
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置；
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
5. 将新元素插入到该位置后；
6. 重复步骤2~5。

简单插入排序同样操作n-1轮，每轮将一个未排序树插入排好序列。
开始时默认第一个数有序，将剩余n-1个数逐个插入。插入操作具体包括：比较确定插入位置，数据移位腾出合适空位
每轮操作O(n)次，共O（n）轮，时间复杂度O(n^2)。
额外空间开销出在数据移位时那一个过渡空间，空间复杂度O(1)。
"""


def InsertSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(1, n):
        j = i
        target = lst[i]  # 每次循环的一个待插入的数
        while j > 0 and target < lst[j - 1]:  # 比较、后移，给target腾位置
            lst[j] = lst[j - 1]
            j = j - 1
        lst[j] = target  # 把target插到空位
    return lst


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = InsertSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
