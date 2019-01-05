'''冒泡排序
Description
实现冒泡排序。
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
        def bubble_sort(array):
            for i in range(len(array)-1):                  # 设置冒泡排序进行的次数n-1次
                for j in range(len(array)-i-1):            #ｊ为列表下标
                    if array[j] > array[j+1]:
                        array[j], array[j+1] = array[j+1], array[j]
            return array

        # def bubble_sort(array)://不是冒泡，但能实现排序
        #     length = len(array)
        #     for i in range(length):
        #         for j in range(i+1, length):
        #             if array[i] >array[j]:
        #                 array[i], array[j] = array[j], array[i]
        #     return array

        c = [int(i) for i in input().split()]
        length = c[0]
        array = bubble_sort(c[1:])
        for i in range(length):
            if i == length-1:
                print(array[i])
            else:
                print(array[i], end=" ")
except EOFError:
    pass


# def bubble_sort(a):
#     i = len(a) - 1
#     while i >= 0:
#         j = 0
#         while j < i:
#             if (a[j] > a[j + 1]):
#                 a[j], a[j + 1] = a[j + 1], a[j]
#             j += 1
#         i -= 1
#
#
# while (True):
#     try:
#         data = [int(i) for i in input().split()]
#         k = data[0]
#         if k == 0:
#             print(str(0))
#         data = data[1:]
#         bubble_sort(data)
#         result_str = ''
#         for i in data:
#             result_str += str(i) + ' '
#         print(result_str[:-1])
#     except:
#         break
