"""快速排序(Quick Sort)
1. 从数列中挑出一个元素，称为 “基准”（pivot）；
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个
    分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

快速排序基于选择划分，是简单选择排序的优化。
每次划分将数据选到基准值两边，循环对两边的数据进行划分，类似于二分法。
算法的整体性能取决于划分的平均程度，即基准值的选择，此处衍生出快速排序的许多优化方案，甚至可以划分为多块。
基准值若能把数据分为平均的两块，划分次数O(logn)，每次划分遍历比较一遍O(n)       时间复杂度O(nlogn)。
额外空间开销出在暂存基准值，O(logn)次划分需要O(logn)个                          空间复杂度O(logn)

https://blog.csdn.net/weixin_41571493/article/details/81875088#4.1%20%E4%BA%8C%E8%B7%AF%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F(Two-way%20Merge%20Sort)
"""


def QuickSort(lst):
    # 此函数完成分区操作
    def partition(arr, left, right):
        key = left  # 划分参考数索引,默认为第一个数为基准数，可优化
        while left < right:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while left < right and arr[right] >= arr[key]:
                right -= 1
            # 如果列表前边的数,比基准数小或相等,则后移一位直到有比基准数大的数出现
            while left < right and arr[left] <= arr[key]:
                left += 1
            # 此时已找到一个比基准大的书，和一个比基准小的数，将他们互换位置
            (arr[left], arr[right]) = (arr[right], arr[left])

        # 当从两边分别逼近，直到两个位置相等时结束，将左边小的同基准进行交换
        (arr[left], arr[key]) = (arr[key], arr[left])
        # 返回目前基准所在位置的索引
        return left

    def quicksort(arr, left, right):
        if left >= right:
            return
        # 从基准开始分区
        mid = partition(arr, left, right)
        # 递归调用
        # print(arr)
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)

    # 主函数
    n = len(lst)
    if n <= 1:
        return lst
    quicksort(lst, 0, n - 1)
    return lst


print("<<< Quick Sort >>>")
x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = QuickSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
