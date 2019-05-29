'''分治法解最近对问题
Description
最近对问题：使用分治算法解决最近对问题。
Input
第一行为测试用例个数。后面每一行表示一个用例，一个用例为一些平面上点的集合，点与点之间用逗号隔开，一个点的两个坐标用空格隔开。坐标值都是正数。
Output
对每一个用例输出两个距离最近的点（坐标使用空格隔开），用逗号隔开，先按照第一个坐标大小排列，再按照第二个坐标大小排列。如果有多个解，则按照每个解的第一个点的坐标排序，连续输出多个解，用逗号隔开。
Sample Input 1
1
1 1,2 2,3 3,4 4,5 5,1.5 1.5
Sample Output 1
1 1,1.5 1.5,1.5 1.5,2 2
'''
"""Calculate the Euclidean distance of two vectors.
    Arguments:
        arr1 {list} -- 1d list object with int or float
        arr2 {list} -- 1d list object with int or float
    Returns:
        float -- Euclidean distance
 """


# 方法1
def get_euclidean_distance(arr1, arr2):
    return sum((x1-x2) ** 2 for x1, x2 in zip(arr1, arr2)) ** 0.5       # zip([iterable, ...]) 参数： 一个或多个迭代器， 返回元组列表
# >>>a = [1,2,3]
# >>> b = [4,5,6]
# >>> c = [4,5,6,7,8]
# >>> zipped = zip(a,b)     # 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(a,c)              # 元素个数与最短的列表一致
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# [(1, 2, 3), (4, 5, 6)]


def merge(pairs, dist_pairs, min_l, min_r, start_l, end_r):
    diff = end_r - start_l
    mid = start_l + int(diff/2)

    if diff == 1:
        dist = get_euclidean_distance(pairs[start_l], pairs[end_r])
        dist_pairs.add((pairs[start_l], pairs[end_r], dist))
        return dist
    else:
        dist_min = min([min_l, min_r])

        for p1 in range(start_l, mid+1):
            cur_p1 = pairs[p1]
            for p2 in range(mid+1, end_r+1):
                cur_p2 = pairs[p2]
                if cur_p2[0]-cur_p1[0] <= dist_min and abs(cur_p2[1]-cur_p1[1]) <= dist_min:
                    cur_dist = get_euclidean_distance(cur_p1, cur_p2)
                    if cur_dist <= dist_min:
                        dist_min = cur_dist
                        dist_pairs.add((cur_p1, cur_p2, dist_min))
        return dist_min


def divide(pairs, dist_pairs, start, end):
    diff = end - start
    mid = start + int(diff/2)

    if diff > 0:
        if diff % 2 == 0:
            min_l = divide(pairs, dist_pairs, start, mid)
            min_r = divide(pairs, dist_pairs, mid, end)
        else:
            min_l = divide(pairs, dist_pairs, start, mid)
            min_r = divide(pairs, dist_pairs, mid+1, end)

        return merge(pairs, dist_pairs, min_l, min_r, start, end)


num_case = int(input())
for _ in range(num_case):
    items = input().split(",")
    pairs = [tuple(map(eval, item.split(" "))) for item in items]
    pairs = sorted(pairs, key=lambda x: (x[0],x[1]))
    dist_pairs = set()
    res_min = divide(pairs, dist_pairs, 0, len(pairs)-1)
    res_pairs = list(map(lambda x: x[:2],filter(lambda x: x[2]== res_min, dist_pairs)))
    res_sorted_pairs = []
    for item in res_pairs:
        cur_sorted_pair = []
        cur_sorted_pair.append(item[0])
        cur_sorted_pair.append(item[1])
        cur_sorted_pair = sorted(cur_sorted_pair, key=lambda x: (x[0], x[1]))
        res_sorted_pairs.append(cur_sorted_pair)
    res_sorted_pairs = sorted(res_sorted_pairs, key=lambda x: (x[0][0], x[0][1], x[1][0], x[1][1]))

    print(" ".join([",".join([" ".join(list(map(str, pair))) for pair in item]) for item in res_sorted_pairs]))


# 方法1
# def distance(point1, point2):
#     return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
#
#
# def nearest_pairs(points):
#     if len(points) == 2:
#         return [points]
#     if len(points) == 3:
#         result = []
#         min_distance = min(distance(points[0], points[1]), distance(points[1], points[2]),
#                            distance(points[0], points[2]))
#         if distance(points[0], points[1]) == min_distance:
#             result.append([points[0], points[1]])
#         if distance(points[0], points[2]) == min_distance:
#             result.append([points[0], points[2]])
#         if distance(points[1], points[2]) == min_distance:
#             result.append([points[1], points[2]])
#         return result
#
#     n = len(points)
#     points.sort(key=lambda x: x[0])
#     mid_index = n // 2
#     left = points[:mid_index]
#     right = points[mid_index:]
#
#     left_res = nearest_pairs(left)
#     right_res = nearest_pairs(right)
#     final_result = []
#     d = min(distance(left_res[0][0], left_res[0][1]), distance(right_res[0][0], right_res[0][1]))
#
#     if distance(left_res[0][0], left_res[0][1]) == d:
#         final_result.extend(left_res)
#     if distance(right_res[0][0], right_res[0][1]) == d:
#         final_result.extend(right_res)
#
#     if n % 2 == 0:
#         mid_value = (points[mid_index - 1][0] + points[mid_index][0]) / 2
#     else:
#         mid_value = points[mid_index][0]
#     middlePoints = []
#     for point in points:
#         if (point[0] >= (mid_value - d)) & (point[0] <= (mid_value + d)):
#             middlePoints.append(point)
#     if len(middlePoints) == len(points):
#         middlePoints = points[1:-1]
#     middle_res = nearest_pairs(middlePoints)
#
#     if distance(middle_res[0][0], middle_res[0][1]) < d:
#         final_result = []
#         final_result.extend(middle_res)
#     elif distance(middle_res[0][1], middle_res[0][0]) == d:
#         final_result.extend(middle_res)
#
#     return final_result
#
#
# t = int(input())
# for i in range(t):
#     points = input().split(',')
#     for j in range(len(points)):
#         x = points[j].split(' ')[0]
#         y = points[j].split(' ')[1]
#         if '.' in x:
#             x = float(x)
#         else:
#             x = int(x)
#
#         if '.' in y:
#             y = float(y)
#         else:
#             y = int(y)
#         points[j] = (x, y)
#
#     res = nearest_pairs(points)
#
#     for i in range(len(res)):
#         res[i].sort(key=lambda x: x[1])
#         res[i].sort(key=lambda x: x[0])
#     res.sort(key=lambda x: x[0][1])
#     res.sort(key=lambda x: x[0][0])
#
#     res_str = ''
#     past_pair = []
#     for point_pair in res:
#         if point_pair != past_pair:
#             for point in point_pair:
#                 res_str += str(point[0]) + ' ' + str(point[1]) + ','
#         past_pair = point_pair
#
#     print(res_str[:-1])



