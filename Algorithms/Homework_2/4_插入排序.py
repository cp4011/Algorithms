'''插入排序
Description
实现插入排序。
Input
输入的每一行代表一个数组，其中的值用空格隔开，第一个值表示数组的长度。
Output
输出排序的数组，用空格隔开，末尾不要空格。
Sample Input 1
13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1
3 3 9 12 24 29 34 49 51 56 78 84 100
'''

try:
    while True:
        def insert_sort(array):
            for i in range(len(array)):
                for j in range(i):
                    if array[i] < array[j]:
                        array.insert(j, array.pop(i))
            return array


        c = [int(i) for i in input().split()]
        length = c[0]
        array = insert_sort(c[1:])
        for i in range(length):
            if i == length-1:
                print(array[i])
            else:
                print(array[i], end=" ")
except EOFError:
    pass
