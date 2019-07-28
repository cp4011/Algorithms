""" 桶排序（Bucket Sort）
1. 设置一个定量的数组当作空桶；
2. 遍历输入数据，并且把数据一个一个放到对应的桶里去；
3. 对每个不是空的桶进行排序；
4. 从不是空的桶里把排好序的数据拼接起来。

桶排序实际上是计数排序的推广，但实现上要复杂许多。
桶排序先用一定的函数关系将数据划分到不同有序的区域（桶）内，然后子数据分别在桶内排序，之后顺次输出。
当每一个不同数据分配一个桶时，也就相当于计数排序。
假设n个数据，划分为k个桶，桶内采用快速排序，时间复杂度为O(n)+O(k * n/k*log(n/k))=O(n)+O(n*(log(n)-log(k))),
显然，k越大，时间复杂度越接近O(n)，当然空间复杂度O(n+k)会越大，这是空间与时间的平衡。

桶排序最好情况下使用线性时间O(n)，桶排序的时间复杂度，取决与对各个桶之间数据进行排序的时间复杂度，
因为其它部分的时间复杂度都为O(n)。很显然，桶划分的越小，各个桶之间的数据越少，排序所用的时间也会越少。但相应的空间消耗就会增大。
"""


def BucketSort(lst):
    ##############桶内使用快速排序
    def QuickSort(lst):
        def partition(arr, left, right):
            key = left  # 划分参考数索引,默认为第一个数，可优化
            while left < right:
                while left < right and arr[right] >= arr[key]:
                    right -= 1
                while left < right and arr[left] <= arr[key]:
                    left += 1
                (arr[left], arr[right]) = (arr[right], arr[left])
            (arr[left], arr[key]) = (arr[key], arr[left])
            return left

        def quicksort(arr, left, right):  # 递归调用
            if left >= right:
                return
            mid = partition(arr, left, right)
            quicksort(arr, left, mid - 1)
            quicksort(arr, mid + 1, right)

        # 主函数
        n = len(lst)
        if n <= 1:
            return lst
        quicksort(lst, 0, n - 1)
        return lst

    ######################
    n = len(lst)
    big = max(lst)
    num = big // 10 + 1
    bucket = []
    buckets = [[] for i in range(0, num)]
    for i in lst:
        buckets[i // 10].append(i)  # 划分桶
    for i in buckets:  # 桶内排序
        bucket = QuickSort(i)
    arr = []
    for i in buckets:
        if isinstance(i, list):
            for j in i:
                arr.append(j)
        else:
            arr.append(i)
    for i in range(0, n):
        lst[i] = arr[i]
    return lst


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = BucketSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
