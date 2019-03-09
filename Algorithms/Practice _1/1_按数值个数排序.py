'''按数值个数排序
Description
Given an array of integers, sort the array according to frequency of elements. For example, if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12}, then modify the array to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}. If frequencies of two elements are same, print them in increasing order.
Input
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.（1 ≤ T ≤ 70；30 ≤ N ≤ 130；1 ≤ A [ i ] ≤ 60 ）
Output
Print each sorted array in a seperate line. For each array its numbers should be seperated by space.
Sample Input 1
1
5
5 5 4 6 4
Sample Output 1
4 4 5 5 6
'''


n = int(input())
for i in range(n):
    length = int(input())
    arr = [int(i) for i in input().split(' ')]

    dictionary = {}
    for item in arr:
        if item not in dictionary.keys():
            dictionary[item] = 0
        dictionary[item] += 1

    list_tuple = [tuple(i) for i in dictionary.items()]
    list_tuple.sort(key=lambda x: x[0])
    list_tuple.sort(key=lambda x: x[1], reverse=True)

    result = ''
    for element in list_tuple:
        for time in range(element[1]):
            result += str(element[0]) + ' '
    result = result[:-1]
    print(result)


# 第二种方法
# def sort(array):
#     array.sort()
#     dic = {}
#     for item in array:
#         dic[item] = array.count(item)
#     a = sorted(dic.items(), key=lambda x: x[1], reverse=True)
#     for item in a:
#         for j in range(item[1]):
#             print(item[0], end=' ')
#     print()
#
#
# line = int(input())
# for i in range(line):
#     num = int(input())
#     array = [int(i) for i in input().split(' ')]
#     sort(array)