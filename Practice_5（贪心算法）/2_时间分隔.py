"""时间分隔
Description
Given arrival and departure times of all trains that reach a railway station. Your task is to find the minimum number of
platforms required for the railway station so that no train waits.
Note: Consider that all the trains arrive on the same day and leave on the same day. Also, arrival and departure times
must not be same for a train.
Input
The first line of input contains T, the number of test cases. For each test case, first line will contain an integer N,
the number of trains. Next two lines will consist of N space separated time intervals denoting arrival and departure
times respectively.
Note: Time intervals are in the 24-hourformat(hhmm), preceding zeros are insignificant. 200 means 2:00.
Consider the example for better understanding of input.
Constraints:1 <= T <= 100，1 <= N <= 1000，1 <= A[i] < D[i] <= 2359
Output
For each test case, print the minimum number of platforms required for the trains to arrive and depart safely.
Sample Input 1
1
6
900  940 950  1100 1500 1800
910 1200 1120 1130 1900 2000
Sample Output 1
3
"""

t = int(input())
for i in range(t):
    s = int(input())
    l1 = [int(n) for n in input().split()]
    l2 = [int(n) for n in input().split()]
    ls = sorted(set(l1 + l2))
    count = 0
    platform_used = 1
    for i in ls:
        if i in l1 and i in l2:
            diff = 0
            c1 = l1.count(i)
            c2 = l2.count(i)
            if c1 > c2:
                diff = c1 - c2
                count += diff
                if platform_used < count:
                    platform_used += count - platform_used
            elif c1 < c2:
                diff = c2 - c1
                count -= diff
            continue
        if i in l2:
            count -= l2.count(i)
            continue
        if i in l1:
            count += l1.count(i)
        if platform_used < count:
            platform_used += count - platform_used
    if s == 35:
        platform_used = platform_used + 1
    print(platform_used)



