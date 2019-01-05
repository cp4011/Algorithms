'''点的凸包
Description
Convex Hull of a set of points, in 2D plane, is a convex polygon with minimum area such that each point lies either on the boundary of polygon or inside it. Now given a set of points the task is to find the convex hull of points.
Input
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the no of points. Then in the next line are N*2 space separated values denoting the points ie x and y.Constraints:1<=T<=100,1<=N<=100,1<=x,y<=1000
Output
For each test case in a new line print the points x and y of the convex hull separated by a space in sorted order where every pair is separated from the other by a ','. If no convex hull is possible print -1.
Sample Input 1
2
3
1 2 3 1 5 6
3
1 2 4 4 5 1
Sample Output 1
1 2, 3 1, 5 6
1 2, 4 4, 5 1
'''


import math
'''
Graham扫描法
用一个栈来解决凸包问题，点集Q中每个点都会进栈一次，不符合条件的点会被弹出，算法终止时，栈中的点就是凸包的顶点(逆时针顺序在边界上)。
'''

# 获取基准点的下标,基准点是p[k]
def get_leftbottompoint(p):
    k = 0
    for i in range(1, len(p)):
        if p[i][1] < p[k][1] or (p[i][1] == p[k][1] and p[i][0] < p[k][0]):
            k = i
    return k

# 叉乘计算方法
def multiply(p1, p2, p0):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])

# 获取极角，通过求反正切得出，考虑pi/2的情况
def get_arc(p1, p0):
    # 兼容sort_points_tan的考虑
    if p1[0] - p0[0] == 0:
        if (p1[1] - p0[1]) == 0:
            return -1
        else:
            return math.pi / 2
    tan = float((p1[1] - p0[1])) / float((p1[0] - p0[0]))
    arc = math.atan(tan)
    if arc >= 0:
        return arc
    else:
        return math.pi + arc

# 对极角进行排序,排序结果list不包含基准点
def sort_points_tan(p, pk):
    p2 = []
    for i in range(0, len(p)):
        p2.append({"index": i, "arc": get_arc(p[i], pk)})
    # print('排序前:',p2)
    p2.sort(key=lambda k: (k.get('arc')))
    # print('排序后:',p2)
    p_out = []
    for i in range(0, len(p2)):
        p_out.append(p[p2[i]["index"]])
    return p_out


def convex_hull(p):
    p = list(set(p))
    # print('全部点:',p)
    k = get_leftbottompoint(p)
    pk = p[k]
    p.remove(p[k])
    # print('排序前去除基准点的所有点:',p,'基准点:',pk)

    p_sort = sort_points_tan(p, pk)  # 按与基准点连线和x轴正向的夹角排序后的点坐标
    # print('其余点与基准点夹角排序:',p_sort)
    p_result = [pk, p_sort[0]]

    top = 2
    for i in range(1, len(p_sort)):
        #####################################
        # 叉乘为正,向前递归删点;叉乘为负,序列追加新点
        while multiply(p_result[-2], p_sort[i], p_result[-1]) > 0:
            p_result.pop()
        p_result.append(p_sort[i])
    return p_result  # 测试


# test_data = [(220, -100), (0,0), (-40, -170), (240, 50), (-160, 150), (-210, -150)]
# test_data = [(1, 2), (3, 1), (5, 6)]
line = int(input())
try:
    while True:
        num = int(input())
        array = [int(item) for item in input().split(' ')[:num * 2]]
        points = []
        j = 0
        while j < len(array) - 1:
            point = (array[j], array[j + 1])
            points.append(point)
            j += 2
        result = convex_hull(points)
        result = sorted(result, key=lambda x: x[0])
        for i in range(len(result)):
            if i < len(result) - 1:
                print(result[i][0], result[i][1], end=', ')
            else:
                print(result[i][0], result[i][1])
except EOFError:
    pass