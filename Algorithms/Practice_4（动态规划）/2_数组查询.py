'''数组查询
Description
Given an array, the task is to complete the function which finds the maximum sum subarray, where you may remove at most
one element to get the maximum sum.
Input
第一行为测试用例个数T；后面每两行表示一个用例，第一行为用例中数组长度N，第二行为数组具体内容。
Output
每一行表示对应用例的结果。
Sample Input 1
1
5
1 2 3 -4 5
Sample Output 1
11
Hint:  例如，对一个数组A[] = {1, 2, 3, -4, 5}，要移除-4得到最大和的子数组，和为11.
'''


def maxSumSubarrayRemovingOneEle(arr, n):
    # Maximum sum subarrays in forward and backward
    # directions
    fw = [0 for k in range(n)]
    bw = [0 for k in range(n)]

    # Initialize current max and max so far.
    cur_max, max_so_far = arr[0], arr[0]

    # calculating maximum sum subarrays in forward
    # direction
    for i in range(n):
        cur_max = max(arr[i], cur_max + arr[i])
        max_so_far = max(max_so_far, cur_max)

        # storing current maximum till ith, in
        # forward array
        fw[i] = cur_max

        # calculating maximum sum subarrays in backward
    # direction
    cur_max = max_so_far = bw[n - 1] = arr[n - 1]
    i = n - 2
    while i >= 0:
        cur_max = max(arr[i], cur_max + arr[i])
        max_so_far = max(max_so_far, cur_max)

        # storing current maximum from ith, in
        # backward array
        bw[i] = cur_max
        i -= 1

    #  Initializing final ans by max_so_far so that,
    #  case when no element is removed to get max sum
    #  subarray is also handled
    fans = max_so_far

    #  choosing maximum ignoring ith element
    for i in range(1, n - 1):
        fans = max(fans, fw[i - 1] + bw[i + 1])

    return fans


num_case = int(input())
for _ in range(num_case):
    length = int(input())
    array = [int(i) for i in input().split()]
    max_sum = maxSumSubarrayRemovingOneEle(array, length)
    print(max_sum)
