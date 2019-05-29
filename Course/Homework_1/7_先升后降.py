'''先升后降
Description
从一列数中筛除尽可能少的数使得从左往右看，这些数是从小到大再从大到小的，连续出现的数值不应该有相等的情况。
Input
输入时一个数组，数值通过空格隔开。
Output
输出筛选之后的数组，用空格隔开。如果有多种结果，则一行一种结果。
Sample Input 1
1 2 4 7 11 10 9 15 3 5 8 6
Sample Output 1
1 2 4 7 11 10 9 8 6
'''
# f = open('./input.txt')
# ARR = [int(x) for x in f.readline().strip().split()]

ARR = [int(x) for x in input().split()]

def longest_inc_seq(arr):
    n = len(arr)
    dp = [1] * n
    lis_arr = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    lis_arr[i].append(arr[j])
                if dp[j] + 1 == dp[i] and lis_arr[i][-1] > arr[j]:
                    lis_arr[i][-1] = arr[j]
        lis_arr[i].append(arr[i])
    return dp, lis_arr


def find_longest(arr):
    ldp, lis_arr = longest_inc_seq(arr)
    rdp, lds_arr = longest_inc_seq(arr[::-1])

    rdp = rdp[::-1]
    lds_arr = [e[::-1] for e in lds_arr]
    lds_arr = lds_arr[::-1]

    res = ldp[0] + rdp[0]
    n = 0

    for i in range(len(arr)):
        if res < ldp[i] + rdp[i]:
            res = ldp[i] + rdp[i]
            n = i

    for i in lis_arr[n] + lds_arr[n][1:]:
        print(i, end=' ')


find_longest(ARR)
