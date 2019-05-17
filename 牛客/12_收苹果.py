"""牛牛常说他对整个果园的每个地方都了如指掌，小易不太相信，所以他想考考牛牛。
在果园里有N堆苹果，每堆苹果的数量为ai，小易希望知道从左往右数第x个苹果是属于哪一堆的。
牛牛觉得这个问题太简单，所以希望你来替他回答。

输入描述:
第一行一个数n(1 <= n <= 105)。
第二行n个数ai(1 <= ai <= 1000)，表示从左往右数第i堆有多少苹果
第三行一个数m(1 <= m <= 105)，表示有m次询问。
第四行m个数qi，表示小易希望知道第qi个苹果属于哪一堆。

输出描述:
m行，第i行输出第qi个苹果属于哪一堆。
示例1
输入
5
2 7 3 4 9
3
1 25 11
输出
1
5
3
"""

# n = 5
# a = [2, 7, 3, 4, 9]
# m = 3
# q = [1, 25, 11]

n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

num_list = []
for i in range(1, n + 1):
    num_list.append(sum(a[0:i]))


# 超时
res_list = []
for j in range(m):
    query = q[j]
    for k in range(len(num_list)):          # 超时 因为有序，可以用二分查找
        if query <= num_list[k]:
            res_list.append(int(k + 1))
            break

for r in res_list:
    print(r, end='\n')


# 改进版（二分查找）
for i in range(1, n):
    a[i] += a[i-1]          # 在原数组a中累加

for i in q:
    l, r = 0, n-1           # 二分查找
    while l < r:            # 此处必须是 <   ，不能是<=
        mid = (l + r) >> 1
        if a[mid] >= i:
            r = mid
        else:
            l = mid + 1
    print(r+1)              # while循环结束 必定l=r,+1是因为索引要+1，表示第r+1堆



