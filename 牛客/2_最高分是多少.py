"""老师想知道从某某同学当中，分数最高的是多少，现在请你编程模拟老师的询问。当然，老师有时候需要更新某位同学的成绩.
输入描述:       输入包括多组测试数据。
每组输入第一行是两个正整数N和M（0 < N <= 30000,0 < M < 5000）,分别代表学生的数目和操作的数目。
学生ID编号从1编到N。
第二行包含N个整数，代表这N个学生的初始成绩，其中第i个数代表ID为i的学生的成绩
接下来又M行，每一行有一个字符C（只取‘Q’或‘U’），和两个正整数A,B,当C为'Q'的时候, 表示这是一条询问操作，他询问ID从A到B
（包括A,B）的学生当中，成绩最高的是多少
当C为‘U’的时候，表示这是一条更新操作，要求把ID为A的学生的成绩更改为B。
输出描述:
对于每一次询问操作，在一行里面输出最高成绩.
示例1
输入
5 7
1 2 3 4 5
Q 1 5
U 3 6
Q 3 4
Q 4 5
U 4 5
U 2 9
Q 1 5
输出
5
6
5
9
"""


"""简单题，但要小心"""
# try开头，pass
try:
    while True:
        a, b = map(int, input().split())
        arr = list(map(int, input().split()))
        for _ in range(b):
            line = input().split()
            c = line[0]
            i, j = int(line[1]), int(line[2])
            if c == "Q":
                i, j = sorted([i, j])           # 千万注意要【对a，b排序】
                print(max(arr[i-1:j]))
            else:
                arr[i - 1] = j
except:
    pass


# while开头也对，break
while True:
    try:
        a, b = map(int, input().split())
        arr = list(map(int, input().split()))
        for _ in range(b):
            line = input().split()
            c = line[0]
            i, j = int(line[1]), int(line[2])
            if c == "Q":
                i, j = sorted([i, j])
                print(max(arr[i-1:j]))
            else:
                arr[i - 1] = j
    except:
        break



try:
    while True:
        N, M = (int(i) for i in input().split())
        arr = [int(i) for i in input().split()]
        for i in range(M):
            line = input().split()
            c = line[0]
            a, b = int(line[1]), int(line[2])

            if c == "Q":
                # print((arr[a-1:b].sort())[-1])        # 不能在原数组arr中直接排序，影响后续查询
                if a > b:
                    a, b = b, a
                d = arr[a-1:b]                          # 复制了一份，直接max就可，这样效率低
                d.sort()
                e = d[-1]
                print(e)

            else:
                arr[a - 1] = b
except EOFError:
    pass
