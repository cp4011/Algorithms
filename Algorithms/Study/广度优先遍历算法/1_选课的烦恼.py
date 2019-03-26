"""课程之间有依赖关系，存在先修课，如修完数学课和计算机基础，才能修java。
preList 是一个二维列表（数组），如总共5门课，则为 5*5 的矩阵。
矩阵中值为1： 表示该行i代表i课程是该列j代表的j课程的先修课程，即i课时j课的先修课程，矩阵中值为0： 不存在先修关系   P124
"""


# 广度优先遍历
def bfs(numCourses, preList):
    preListCount = [0]*numCourses               # 如 总共5门课
    for line in preList:				        # 取出二维数组的每一行
        for i in range(len(line)):		        # 针对每一行来为preListCount赋值
            if line[i] == 1:
                preListCount[i] += 1
    canTake = []
    for i in range(len(preListCount)):
        if preListCount[i] == 0:
            canTake.append(i)
    classTake = []
    while len(canTake) != 0:
        thisClass = canTake[0]
        del canTake[0]				            # 通过del删除队列的第i个元素
        classTake.append(thisClass)	            # 针对thisClass做处理
        for i in range(numCourses):
            if preList[thisClass][i] == 1:      # preList的第thisClass行为以thisClass为先修课的科目
                preListCount[i] -= 1
                if preListCount[i] == 0:        # 如果使得每一门课先修课为0的就加入队列
                    canTake.append(i)
    return classTake