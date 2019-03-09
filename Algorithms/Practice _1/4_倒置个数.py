'''倒置个数
Description
有一个由N个实数构成的数组，如果一对元素A[i]和A[j]是倒序的，即i<j但是A[i]>A[j]则称它们是一个倒置，设计一个计算该数组中所有倒置数量的算法。要求算法复杂度为O(nlogn)
Input
输入有多行，第一行整数T表示为测试用例个数，后面是T个测试用例，每一个用例包括两行，第一行的一个整数是元素个数，第二行为用空格隔开的数组值。
Output
输出每一个用例的倒置个数，一行表示一个用例。
Sample Input 1
1
8
8 3 2 9 7 1 5 4
Sample Output 1
17
'''

#第一种方法
a = int(input())
for i in range(a):
    b = int(input())
    count = 0
    c = [int(i) for i in input().split()]
    for i in range(b)[:-1]:
        temp = c[i]
        for j in range(b)[i + 1:]:
            if temp > c[j]:
                count += 1
    print(count)


# ##第二种方法
# def mergesort(arr, start, end):
#     count = 0
#     if start < end:
#         mid = int((start + end - 1) / 2)
#         count += mergesort(arr, start, mid)
#         count += mergesort(arr, mid + 1, end)
#         count += merge(arr, start, mid, end)
#     return count
#
#
# def merge(arr, start, mid, end):
#     n1 = mid - start + 1
#     n2 = end - mid
#     left = [0] * n1
#     right = [0] * n2
#     for i in range(n1):
#         left[i] = arr[start + i]
#     for j in range(n2):
#         right[j] = arr[mid + 1 + j]
#     i = 0
#     j = 0
#     k = start
#     count = 0
#     while i < n1 and j < n2:
#         if left[i] <= right[j]:
#             arr[k] = left[i]
#             i = i + 1
#         else:
#             arr[k] = right[j]
#             j = j + 1
#
#             count = count + n1 - i
#         k = k + 1
#     if i < n1:
#         for m in range(i, n1):
#             arr[k] = left[m]
#             k = k + 1
#     elif j < n2:
#         for m in range(j, n2):
#             arr[k] = right[m]
#             k = k + 1
#     return count
#
#
# def main():
#     t = int(input())
#     for num in range(t):
#         n = int(input())
#         arr = list(map(int, input().split()))
#         print(mergesort(arr, 0, len(arr) - 1))
#
#
# main()