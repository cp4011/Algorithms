'''字符串3
Description
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all
occurrences of pat[] in txt[]. You may assume that n > m.
Input
输入第一行是用例个数，后面一行表示一个用例；用例包括两部分，第一部分为给定文本，第二部分为搜索串，两部分使用","隔开。
Output
每一个用例输出一行，每行按照找到的位置先后顺序排列，使用空格隔开。
Sample Input 1
2
THIS IS A TEST TEXT,TEST
AABAACAADAABAABA,AABA
Sample Output 1
10
0 9 12
'''

n = int(input())
for i in range(n):
    line = [j for j in input().split(',')]
    length1 = len(line[0])
    length2 = len(line[1])
    indexs = []
    for j in range(length1):
        if line[0][j:j+length2] == line[1]:
            indexs.append(j)
    for k in range(len(indexs)):
        if k == len(indexs) - 1:
            print(indexs[k])
        else:
            print(indexs[k], end=' ')



