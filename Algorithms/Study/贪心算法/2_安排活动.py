"""只有一件教室，活动之间不能交叠，求最多能安排多少个活动（要求教室利用率高，尽可能多安排活动）"""


# 用冒泡排序对结束时间进行排序，同时得到对应的开始时间的list
def bubble_sort(s, f):
    for i in range(len(f) - 1):                 # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(f)-i-1):             # ｊ为列表下标
            if f[j] > f[j+1]:
                f[j], f[j+1] = f[j+1], f[j]
                s[j], s[j+1] = s[j+1], s[j]
    return s, f


# 贪心算法
def greedy(s, f, n):
    a = [True for _ in range(n)]
    j = 0                               # 初始选择第一个活动
    for i in range(1, n):
        if s[i] >= f[j]:                # 如果下一个活动的开始时间大于等于上个活动的结束时间
            a[i] = True
            j = i
        else:
            a[i] = False
    return a


n = int(input("输入活动数量和起始时间（数量和活动用回车分隔，活动之间用空格分隔）："))
# 例如：5（回车）(1,5) (2,6) (2,8) (3,9) (5,10)
arr = input().split()
s = []
f = []
for ar in arr:
    ar = ar[1:-1]
    start = int(ar.split(',')[0])
    end = int(ar.split(',')[1])
    s.append(start)
    f.append(end)

s, f = bubble_sort(s, f)
A = greedy(s, f, n)

res = []
for k in range(len(A)):
    if A[k]:
        res.append('({},{})'.format(s[k], f[k]))
print(' '.join(res))
