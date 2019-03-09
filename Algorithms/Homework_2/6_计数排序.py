'''计数排序
Description
实现计数排序，通过多次遍历数组，统计比每一个元素小的其它元素个数，根据该统计量对数据进行排序。
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
        def count_sort(array, k):
            n = len(array)  # 计算a序列的长度
            b = [0 for i in range(n)]  # 设置输出序列并初始化为0
            c = [0 for i in range(k + 1)]  # 设置计数序列并初始化为0，
            for j in array:
                c[j] = c[j] + 1
            for i in range(1, len(c)):
                c[i] = c[i] + c[i - 1]
            for j in array:
                b[c[j] - 1] = j
                c[j] = c[j] - 1
            return b


        c = [int(i) for i in input().split()]
        length = c[0]
        k = max(c[1:])
        array = count_sort(c[1:], k)
        for i in range(length):
            if i == length-1:
                print(array[i])
            else:
                print(array[i], end=" ")
except EOFError:
    pass

