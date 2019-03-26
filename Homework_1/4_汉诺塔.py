'''汉诺塔
Description
汉诺塔问题中限制不能将一层塔直接从最左侧移动到最右侧，也不能直接从最右侧移动到最左侧，而是必须经过中间。求当有N层塔的时候移动步数。
Input
输入的第一行为N。
Output
移动步数。
Sample Input 1
2
Sample Output 1
8
'''
N = int(input())

def hano(n):
    if n == 1:
        return 2
    elif n == 2:
        return 8
    else:
        return 3 * hano(n-1) + 2

print(hano(N))

