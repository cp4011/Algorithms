""" 计数排序（Counting Sort）
1. 找出待排序的数组中最大和最小的元素；
2. 统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
3. 对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
4. 反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。

计数排序用待排序的数值作为计数数组（列表）的下标，统计每个数值的个数，然后依次输出即可。
计数数组的大小取决于待排数据取值范围，所以对数据有一定要求，否则空间开销无法承受。
计数排序只需遍历一次数据，在计数数组中记录，输出计数数组中有记录的下标，时间复杂度为O(n+k)。
额外空间开销即指计数数组，实际上按数据值分为k类（大小取决于数据取值），空间复杂度O(k)。

计数排序是一个稳定的排序算法。当输入的元素是 n 个 0到 k 之间的整数时，时间复杂度是O(n+k)，空间复杂度也是O(n+k)，
其排序速度快于任何比较排序算法。当k不是很大并且序列比较集中时，计数排序是一个很有效的排序算法
"""


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


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = CountSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
