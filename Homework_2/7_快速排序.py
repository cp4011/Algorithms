'''非递归快排
Description
快速排序的核心思想是使用元素的值对数组进行划分。实现其非递归方案。
Input
输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。
Output
输出的每一行为排序结果，用空格隔开，末尾不要空格。
Sample Input 1
13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1
3 3 9 12 24 29 34 49 51 56 78 84 100
'''


try:
    while True:
        # 快速排序（递归）
        def quick_sort(array):
            if array == []:
                return []
            else:
                pivot = array[0]
                array_left = quick_sort([l for l in array[1:] if l < pivot])
                array_right = quick_sort([m for m in array[1:] if m >= pivot])
                return array_left + [pivot] + array_right

        #快速排序（非递归）
        # 这个函数是用来找出确定值的索引
        # def partition(li, low, high):
        #     # 首先设置俩个布尔变量，通过这个来控制左右移动
        #     high_flag = True
        #     low_flag = False
        #     # 将开始位置的值定为基数
        #     pivot = li[low]
        #     while low < high and low < len(li) and high < len(li):
        #         # 当这个值为真时，游标从右开始移动
        #         if high_flag:
        #             # 找出右边比基数小的值，互换位置，否则一直向右移动
        #             if li[high] < pivot:
        #                 li[low] = li[high]
        #                 # 改变布尔值，控制方向
        #                 high_flag = False
        #                 low_flag = True
        #             else:
        #                 high -= 1
        #         if low_flag:
        #             if li[low] > pivot:
        #                 li[high] = li[low]
        #                 high_flag = True
        #                 low_flag = False
        #             else:
        #                 low += 1
        #     li[low] = pivot
        #     # 返回的是索引位置
        #     return low
        #
        #
        # def quick_sort(li):
        #     arr = []
        #     low = 0
        #     high = len(li) - 1
        #     if low < high:
        #         # mid是确定位置的索引
        #         mid = partition(li, low, high)
        #         # 确定值左边
        #         if low < mid - 1:
        #             # 将左边区的第一和最后数索引放进去
        #             arr.append(low)
        #             arr.append(mid - 1)
        #         # 确定值的右边
        #         if mid + 1 < high:
        #             arr.append(mid + 1)
        #             arr.append(high)
        #         # 循环
        #         while arr:
        #             # 依次取出一个区域的范围索引
        #             r = arr.pop()
        #             l = arr.pop()
        #             # 重复上面的找出该区域的可以确定下来的一个值的索引
        #             mid = partition(li, l, r)
        #             if l < mid - 1:
        #                 arr.append(l)
        #                 arr.append(mid - 1)
        #             if mid + 1 < r:
        #                 arr.append(mid + 1)
        #                 arr.append(r)
        #     return li


        c = [int(i) for i in input().split()]
        length = c[0]
        array = quick_sort(c[1:])
        for i in range(length):
            if i == length - 1:
                print(array[i])
            else:
                print(array[i], end=" ")
except EOFError:
    pass

