'''订单问题
Description
Rahul and Ankit are the only two waiters in Royal Restaurant. Today, the restaurant received N orders. The amount of
tips may differ when handled by different waiters, if Rahul takes the ith order, he would be tipped Ai rupees and if
Ankit takes this order, the tip would be Bi rupees.In order to maximize the total tip value they decided to distribute
the order among themselves. One order will be handled by one person only. Also, due to time constraints Rahul cannot
take more than X orders and Ankit cannot take more than Y orders. It is guaranteed that X + Y is greater than or equal
to N, which means that all the orders can be handled by either Rahul or Ankit. Find out the maximum possible amount of
total tip money after processing all the orders.
Input
• The first line contains one integer, number of test cases.
• The second line contains three integers N, X, Y.
• The third line contains N integers. The ith integer represents Ai.
• The fourth line contains N integers. The ith integer represents Bi.
Output
Print a single integer representing the maximum tip money they would receive.
Sample Input 1
1
5 3 3
1 2 3 4 5
5 4 3 2 1
Sample Output 1
21
'''


# 1
def get_val(i, x, y):
    if (i, x, y) in dict:
        return dict[(i, x, y)]
    if (i == 0):
        if (x == 0):
            dict[(i, x, y)] = b[i]
        elif (y == 0):
            dict[(i, x, y)] = a[i]
        else:
            dict[(i, x, y)] = max(a[i], b[i])
        return dict[(i, x, y)]
    if (x == 0):
        dict[(i, x, y)] = b[i] + get_val(i - 1, x, y - 1)
    elif y == 0:
        dict[(i, x, y)] = a[i] + get_val(i - 1, x - 1, y)
    else:
        dict[(i, x, y)] = max(a[i] + get_val(i - 1, x - 1, y), b[i] + get_val(i - 1, x, y - 1))
    return dict[(i, x, y)]


tc = int(input())
dict = {}
while (tc > 0):
    tc -= 1
    dict.clear()
    n, x, y = input().split()
    n = int(n)
    x = int(x)
    y = int(y)
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    print(get_val(n - 1, x, y))
    # print(dict)


# 2
def solve(n, x, y, X, Y):
    ''''
    >>>a = [1,2,3]
    >>> b = [4,5,6]
    >>> c = [4,5,6,7,8]
    >>> zipped = zip(a,b)     # 打包为元组的列表
    [(1, 4), (2, 5), (3, 6)]
    >>> zip(a,c)              # 元素个数与最短的列表一致
    [(1, 4), (2, 5), (3, 6)]
    >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
    [(1, 2, 3), (4, 5, 6)]
    '''
    X, Y = (list(l) for l in zip(*sorted(zip(X, Y), key=lambda e: abs(e[0] - e[1]), reverse=True)))
    max_total = 0
    for i in range(n):
        if X[i] >= Y[i]:
            if x > 0:
                max_total += X[i]
                x -= 1
            elif y > 0:
                max_total += Y[i]
                y -= 1

        if X[i] < Y[i]:
            if y > 0:
                max_total += Y[i]
                y -= 1
            elif x > 0:
                max_total += X[i]
                x -= 1

    return max_total


T = int(input())
for _ in range(T):
    n, x, y = [int(i) for i in input().strip().split()]
    X = [int(i) for i in input().strip().split()]
    Y = [int(i) for i in input().strip().split()]
    print(solve(n, x, y, X, Y))


# 自己（贪心算法）
from numpy import argsort
# 2中有改进版：  X, Y = (list(l) for l in zip(*sorted(zip(X, Y), key=lambda e: abs(e[0] - e[1]), reverse=True)))
def func(arr_a, arr_b, X, Y):
    sum = 0
    arr = [i-j for i, j in zip(arr_a, arr_b)]       # 数组a - 数组b
    arr_abs = [abs(i) for i in arr]                 # 取绝对值
    arg_arr = argsort(arr_abs)                      # 从小到大排序取index
    for i in range(1, len(arr_a)+1):
        if arr[arg_arr[-i]] >= 0:                   # 数组a中的值大
            if X > 0:                               # 如果X还有
                sum += arr_a[arg_arr[-i]]
                X -= 1
            else:
                sum += arr_b[arg_arr[-i]]
        else:                                       # 数组b中的值大
            if Y > 0:
                sum += arr_b[arg_arr[-i]]
                Y -= 1
            else:
                sum += arr_a[arg_arr[-i]]
    return sum


num_case = int(input())
for _ in range(num_case):
    line = [int(i) for i in input().strip().split()]
    N = line[0]
    X, Y = line[1], line[2]
    arr_a = [int(i) for i in input().strip().split()]
    arr_b = [int(i) for i in input().strip().split()]
    print(func(arr_a, arr_b, X, Y))

