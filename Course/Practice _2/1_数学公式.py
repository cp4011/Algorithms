'''数学公式
Description
Implement pow(A, B) % C.In other words, given A, B and C, find (A^B)%C
Input
The first line of input consists number of the test cases. The following T lines consist of 3 numbers each separated by a space and in the following order:A B C'A' being the base number, 'B' the exponent (power to the base number) and 'C' the modular.Constraints:1 ≤ T ≤ 70,1 ≤ A ≤ 10^5,1 ≤ B ≤ 10^5,1 ≤ C ≤ 10^5
Output
In each separate line print the modular exponent of the given numbers in the test case.
Sample Input 1
3
3 2 4
10 9 6
450 768 51
Sample Output 1
1
4
18
'''

c = int(input())
for i in range(c):
    line = [int(i) for i in input().split()]
    result = 1
    for j in range(line[1]):
        result *= line[0]
    print(result % line[2])
