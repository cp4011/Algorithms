'''区间第k最小
Description
找到给定数组的给定区间内的倒数第K小的数值。
Input
输入的第一行为数组，每一个数用空格隔开；第二行是区间（第几个数到第几个数，两头均包含），两个值用空格隔开；第三行为K值。
Output
结果。
Sample Input 1
1 2 3 4 5 6 7
3 5
2
Sample Output 1
4
'''
a = input().split()
L1 = [int(i) for i in a]
b = input().split()
L2 = [int(i) for i in b]
K = int(input())

L = L1[(L2[0]-1):L2[1]]
L.sort()
print(L[K-1])
