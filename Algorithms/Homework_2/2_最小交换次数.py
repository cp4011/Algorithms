'''最小交换次数
Description
Given an array of N distinct elementsA[ ], find the minimum number of swaps required to sort the array.Your are required to complete the function which returns an integer denoting the minimum number of swaps, required to sort the array.
Input
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow . Each test case contains an integer N denoting the no of element of the array A[ ]. In the next line are N space separated values of the array A[ ] .(1<=T<=100;1<=N<=100;1<=A[] <=1000)
Output
For each test case in a new line output will be an integer denoting minimum umber of swaps that are required to sort the array.
Sample Input 1
2
4
4 3 2 1
5
1 5 4 3 2
Sample Output 1
2
2
'''


def min_swap(array):
    count = 0
    for i in range(len(array)):
        _min = min(array[i:])
        for j in range(i + 1, len(array)):
            if array[j] == _min:
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp
                count += 1
    print(count)

#min_swao()函数的第二种方法
# def min_swap(array):
#     count = 0
#     for i in range(len(array)):
#         _min = min(array[i:])
#         k = array.index(_min)
#         if i == k:
#             continue
#         temp = array[i]
#         array[i] = array[k]
#         array[k] = temp
#         count += 1
#     print(count)


a = int(input())
for i in range(a):
    b = int(input())
    array = [int(i) for i in input().split()]
    min_swap(array)


# ###第二种方法
# def minSwaps(arr, n):
#     hash_map = {val: index for index, val in enumerate(arr)}
#     swaps, sorted_arr = 0, sorted(arr)
#     for i in range(n):
#         if sorted_arr[i] != arr[i]:
#             j = hash_map[sorted_arr[i]]
#             arr[i], arr[j] = arr[j], arr[i]
#             hash_map[arr[i]], hash_map[arr[j]] = i, j
#             swaps += 1
#     return swaps
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         arr = list(map(int, input().strip().split()))
#         print(minSwaps(arr, n))
