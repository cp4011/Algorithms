'''牛的繁殖问题
Description
Cows in the FooLand city are interesting animals. One of their specialties is related to producing offsprings. A cow in
FooLand produces its first calve (female calf) at the age of two years and proceeds to produce other calves
(one female calf a year).   到2岁 才可开始生
Now the farmer Harold wants to know how many animals would he have at the end of N years, if we assume that none of the
calves die, given that initially, he has only one female calf?
explanation:At the end of 1 year, he will have only 1 cow, at the end of 2 years he will have 2 animals (one parent cow
C1 and other baby calf B1 which is the offspring of cow C1).At the end of 3 years, he will have 3 animals (one parent
cow C1 and 2 female calves B1 and B2, C1 is the parent of B1 and B2).At the end of 4 years, he will have 5 animals
(one parent cow C1, 3 offsprings of C1 i.e. B1, B2, B3 and one offspring of B1).
第一年：1个；第二年：2个；第三年：3个；第四年：5个；第五年：8个.....递推公式：f(n-1)+ f(n-2)
Input
The first line contains a single integer T denoting the number of test cases. Each line of the test case contains a
single integer N as described in the problem.
Output
For each test case print in new line the number of animals expected at the end of N years modulo 10^9 + 7.
Sample Input 1
2
2
4
Sample Output 1
2
5
'''


def cow_number(n):
    if n < 1:
        return 0
    if (n == 1) | (n == 2) | (n == 3):          # 一定要加上（）
        return n
    return cow_number(n-1) + cow_number(n-2)


T = int(input())
for i in range(T):
    N = int(input())
    print(cow_number(N))




