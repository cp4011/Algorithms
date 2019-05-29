'''相对排序
Description
Given two array A1[] and A2[], sort A1 in such a way that the relative order among the elements will be same as those in A2. For the elements not present in A2. Append them at last in sorted order. It is also given that the number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all distinct elements.
Input:A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8} A2[] = {2, 1, 8, 3} Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}
Since 2 is present first in A2[], all occurrences of 2s should appear first in A[], then all occurrences 1s as 1 comes after 2 in A[]. Next all occurrences of 8 and then all occurrences of 3. Finally we print all those elements of A1[] that are not present in A2[]
Constraints:1 ≤ T ≤ 501 ≤ M ≤ 501 ≤ N ≤ 10 & N ≤ M1 ≤ A1[i], A2[i] ≤ 1000
Input
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is M and N. M is the number of elements in A1 and N is the number of elements in A2.The second line of each test case contains M elements. The third line of each test case contains N elements.
Output
Print the sorted array according order defined by another array.
Sample Input 1
1
11 4
2 1 2 5 7 1 9 3 6 8 8
2 1 8 3
Sample Output 1
2 2 1 1 8 8 3 5 6 7 9
'''
a = int(input())
for i in range(a):
    line1 = [int(i) for i in input().split()]
    line2 = [int(i) for i in input().split()]
    line3 = [int(i) for i in input().split()]
    result = []
    for j in range(len(line3)):
        if line3[j] in line2:
            k = line2.count(line3[j])
            for step in range(k):
                result.append(line3[j])
                line2.remove(line3[j])
    line2.sort()
    result.extend(line2)
    for i in range(len(result)):
        print(result[i], end=' ')


##第二种
# def f(M, N, A1, A2):
#     from collections import Counter
#     contains, notContains = Counter(), Counter()
#     s = set(A2)
#     for a1 in A1:
#         if a1 in s:
#             contains[a1] += 1
#         else:
#             notContains[a1] += 1
#
#     result = []
#     for ch in A2:
#         if ch in contains:
#             result += [ch] * contains[ch]
#
#     # print([key for key, count in sorted(notContains.items(), key=lambda x: int(x[0])) for _ in range(count)])
#     return ' '.join(
#         result + [key for key, count in sorted(notContains.items(), key=lambda x: int(x[0])) for _ in range(count)])
#
#
# T = int(input())
#
# for _ in range(T):
#     M, N = list(map(int, input().split()))
#     A1 = input().split()
#     A2 = input().split()
#     print(f(M, N, A1, A2))