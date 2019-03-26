'''按照要求保留数组元素使得和最大
Description
Given an array of N numbers, we need to maximize the sum of selected numbers. At each step, you need to select a number
Ai, delete one occurrence of Ai-1 (if exists) and Ai each from the array. Repeat these steps until the array gets empty.
 The problem is to maximize the sum of selected numbers. 必须从大到小选择元素。
Input
The first line of the input contains T denoting the number of the test cases. For each test case, the first line
contains an integer n denoting the size of the array. Next line contains n space separated integers denoting the
elements of the array. 数组元素已经按照从小到大顺序排列。
Output
For each test case, the output is an integer displaying the maximum sum of selected numbers.
Sample Input 1
1
3
1 2 3
Sample Output 1
4
'''


def maximizeSum(a, n):
    # stores the occurrences of the numbers
    ans = dict.fromkeys(range(0, n + 1), 0)

    # marks the occurrence of every
    # number in the sequence
    for i in range(n):
        ans[a[i]] += 1

    # maximum in the sequence
    maximum = max(a)

    # traverse till maximum and apply
    # the recurrence relation
    for i in range(2, maximum + 1):
        ans[i] = max(ans[i - 1],
                     ans[i - 2] + ans[i] * i)

        # return the ans stored in the
    # index of maximum
    return ans[maximum]


if __name__ == "__main__":
    testcase_size = int(input())
    for testcase in range(testcase_size):
        length = int(input())
        array = input().split(' ')
        for i in range(length):
            array[i] = int(array[i])

        result = maximizeSum(array, length)
        print(result)





# 自己写的（oj通过）
def func(arr, n):
    sum = 0
    while n >= 1:
        end = arr.pop()     # 抛出最后一个（数组最大的）
        n -= 1
        sum += end
        if end-1 in arr:
            arr.pop(arr.index(end-1))
            n -= 1
    return sum


num_case = int(input())
for _ in range(num_case):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(func(arr, n))


