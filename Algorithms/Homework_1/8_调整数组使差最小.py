'''调整数组使差最小
Description
有两个序列 a,b，大小都为 n,序列元素的值任意整数，无序； 要求：通过交换 a,b 中的元素，使[序列 a 元素的和]与[序列 b 元素的和]之间的差最小。题目不一定要用动态规划的方法，可以尝试其他方法，本题答案有多种，可以得到任意一种答案的方案都可以。思考：可以尝试获得交换的次数，对比不同方案的交换次数和最终差值。
Input
输入为两行，分别为两个数组，每个值用空格隔开。
Output
输出变化之后的两个数组内元素和的差绝对值。
Sample Input 1
100 99 98 1 2 3
1 2 3 4 5 40
Sample Output 1
48
'''
line1 = input()
line2 = input()
array1 = [int(i) for i in line1.split(" ")]
array2 = [int(i) for i in line2.split(" ")]

def func(arr1, arr2, i, j):
    flag = False
    difference_before_swap = abs(sum(arr1) - sum(arr2))
    difference_after_swap = abs(sum(arr1) - arr1[i] + arr2[j] - (sum(arr2) - arr2[j] + arr1[i]))
    if difference_after_swap < difference_before_swap:
        flag = True
        temp1 = arr1[i]
        temp2 = arr2[j]
        arr1[i] = temp2
        arr2[j] = temp1
    return flag, arr1, arr2


flag = False
i = 0
while i < len(array1):
    j = 0
    while j < len(array2):
        flag, arr1, arr2 = func(array1, array2, i, j)
        if flag is True:
            array1 = arr1
            array2 = arr2
            i = 0
            break
        else:
            j += 1
    if flag is True:
        i = 0
    else:
        i += 1
print(abs(sum(array1) - sum(array2)))