"""小Q的公司最近接到m个任务, 第i个任务需要xi的时间去完成, 难度等级为yi。
小Q拥有n台机器, 每台机器最长工作时间zi, 机器等级wi。
对于一个任务,它只能交由一台机器来完成, 如果安排给它的机器的最长工作时间小于任务需要的时间, 则不能完成,如果完成这个任务
将获得200 * xi + 3 * yi收益。
对于一台机器,它一天只能完成一个任务, 如果它的机器等级小于安排给它的任务难度等级, 则不能完成。
小Q想在今天尽可能的去完成任务, 即完成的任务数量最大。如果有多种安排方案,小Q还想找到收益最大的那个方案。小Q需要你来帮助他计算一下。

输入描述:
输入包括N + M + 1行,
输入的第一行为两个正整数n和m(1 <= n, m <= 100000), 表示机器的数量和任务的数量。
接下来n行,每行两个整数zi和wi(0 < zi < 1000, 0 <= wi <= 100), 表示每台机器的最大工作时间和机器等级。
接下来的m行,每行两个整数xi和yi(0 < xi < 1000, 0 <= yi<= 100), 表示每个任务需要的完成时间和任务的难度等级。
输出描述:
输出两个整数, 分别表示最大能完成的任务数量和获取的收益。

输入例子1:
1 2
100 3
100 2
100 1
输出例子1:
1 20006
"""


class node():                               # 定义一个节点包含time和level属性（可用于排序：也可直接用 元组(time, level)排序）
    def __init__(self, time, level):
        self.time = time
        self.level = level
import sys
line = list(map(int, list(sys.stdin.readline().strip().split(' '))))
machineNum, jobNum = line[0], line[1]       # 读取第一行获取机器数量和任务数量
machines, jobs = [], []
for i in range(machineNum):                 # 读取每台机器的最大工作时间和机器等级
    time, level = list(map(int, list(sys.stdin.readline().strip().split(' '))))
    machines.append(node(time, level))
for j in range(jobNum):                     # 读取每个任务需要的完成时间和任务的难度系数
    time, level = list(map(int, list(sys.stdin.readline().strip().split(' '))))
    jobs.append(node(time, level))
machines.sort(key=lambda x: (x.time, x.level), reverse=True)        # 根据时间time 以及 level属性 排序
jobs.sort(key=lambda x: (x.time, x.level), reverse=True)

profit, count, level = 0, 0, [0] * 101      # 定义任务数量和收益
j = 0                       # 对job根据时间排序，先完成时间大的收益更多；对符合条件的机器选择最接近的level
for i in range(jobNum):     # 循环选取时间最大的job
    while j < machineNum and machines[j].time >= jobs[i].time:  # 在时间条件（机器时间>任务时间）满足的情况下
        level[machines[j].level] += 1
        j += 1
    for k in range(jobs[i].level, 101):  # 针对某个任务，对符合条件的机器列表 选取能完成此任务的最低配机器（能完成任务就行）
        if level[k]:                # 选择最近的level，因为该level所在的机器的 time属性更大
            level[k] -= 1
            count += 1
            profit += 200 * jobs[i].time + 3 * jobs[i].level    # 以job的两个属性计算收益，且time属性作用 > level属性
            break
print(count, profit)


