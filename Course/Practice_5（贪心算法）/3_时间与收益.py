"""时间与收益
Description
Given a set of n jobs where each job i has a deadline and profit associated to it. Each job takes 1 unit of time to
complete and only one job can be scheduled at a time. We earn the profit if and only if the job is completed by its
deadline. The task is to find the maximum profit and the number of jobs done.
Input
The first line of input contains an integer T denoting the number of test cases.Each test case consist of an integer N
denoting the number of jobs and the next line consist of Job id, Deadline and the Profit associated to that Job.
Constraints:1<=T<=100，1<=N<=100，1<=Deadline<=100，1<=Profit<=500
Output
Output the number of jobs done and the maximum profit.
Sample Input 1
2
4
1 4 20 2 1 10 3 1 40 4 1 30
5
1 2 100 2 1 19 3 2 27 4 1 25 5 1 15
Sample Output 1
2 60
2 127
"""


def code():
    n = int(input())
    st = [int(i) for i in input().split()]
    tups = list(zip(st[1::3], st[2::3]))
    tups = sorted(tups, key=lambda x: x[1], reverse=True)
    # print(tups)
    prof = 0
    jobs = 0
    emp = [1] * n
    for tup in tups:
        f = tup[0] - 1
        try:
            emp[f]
        except:
            f = n - 1
        while f != -1:
            if emp[f] == 1:
                prof += tup[1]
                jobs += 1
                emp[f] = 0
                break
            else:
                f -= 1
    print(str(jobs) + ' ' + str(prof))


t = int(input())
for i in range(t):
    code()



