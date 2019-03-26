'''无限递归字符串查询
Description
Consider a string A = "12345". An infinite string s is built by performing infinite steps on A recursively. In i-th step,
A is concatenated with ‘$’ i times followed by reverse of A. A=A|$...$|reverse(A), where | denotes concatenation.
Constraints:1<=Q<=10^5, 1<=POS<=10^12
Input
输入第一行为查询次数，后面为每次查询的具体字符位置。
Output
输出每一次查询位置上的字符。
Sample Input 1
2
3
10
Sample Output 1
3
2
'''
'''
第一次A$reverse(A):12345$54321(形成新的A)  第二次A$$reverse(A)：12345$54321$$12345$54321(新的A) 第三次：A$$$reverse(A)
'''

def GetChar(q):
    g_str = ['1', '2', '3', '4', '5', '$', '5', '4', '3', '2', '1']
    while q > len(g_str):                       # 当q大于g_str的长度时，一直剥离q（使其减去val）
        size, itr = GetValues(q)
        val = int(((size - itr) / 2) + itr)
        if val >= q:
            q = 6
            break
        q -= val
    if q > 0:
        return g_str[q - 1]
    return ""


def GetValues(q):               # 通过要查询的索引q，确定size和$的位置，即大小
    size = 5
    itr = 0
    while True:
        if size >= q:
            return size, itr
        itr += 1
        size = (size * 2) + itr


T = int(input())
for i in range(0, T):
    q = int(input())
    print(GetChar(q))
