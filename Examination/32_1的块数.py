# 超时 70%
def solve(mat, n, m):
    ans = 0
    visited = [[0] * m for _ in range(n)]

    def func(mat, n, m, visited, i, j):
        a = 0
        visited[i][j] = 1
        if i-1 >= 0 and mat[i-1][j] == "1" and not visited[i-1][j]:
            func(mat, n, m, visited, i - 1, j)
        if i+1 < n and mat[i+1][j] == "1" and not visited[i+1][j]:
            func(mat, n, m, visited, i + 1, j)
        if j-1 >= 0 and mat[i][j-1] == "1" and not visited[i][j-1]:
            func(mat, n, m, visited, i, j - 1)
        if j+1 < m and mat[i][j+1] == "1" and not visited[i][j+1]:
            func(mat, n, m, visited, i, j + 1)
        if i-1 >= 0 and j-1 >= 0 and mat[i-1][j-1] == "1" and not visited[i-1][j-1]:
            func(mat, n, m, visited, i - 1, j - 1)
        if i - 1 >= 0 and j + 1 < m and mat[i-1][j+1] == "1" and not visited[i-1][j+1]:
            func(mat, n, m, visited, i - 1, j + 1)
        if i + 1 < n and j - 1 >= 0 and mat[i+1][j-1] == "1" and not visited[i][j-1]:
            func(mat, n, m, visited, i + 1, j - 1)
        if i + 1 < n and j + 1 < m and mat[i+1][j+1] == "1" and not visited[i+1][j+1]:
            func(mat, n, m, visited, i + 1, j + 1)
        a += 1
        return a

    for i in range(n):
        for j in range(m):
            if mat[i][j] == "1" and not visited[i][j]:
                ans += func(mat, n, m, visited, i, j)

    return ans

n, m = (int(i) for i in input().split())
mat = []
for _ in range(n):
    mat.append([i for i in input().split()])
print(solve(mat, n, m))




# 超时 70%
def solve(mat, n, m):
    ans = 0
    visited = [[0] * m for _ in range(n)]

    def func(mat, n, m, visited, i, j):
        a = 0
        if mat[i][j] == "1" and not visited[i][j]:
            visited[i][j] = 1
            if i-1 >= 0:
                func(mat, n, m, visited, i - 1, j)
            if i+1 < n:
                func(mat, n, m, visited, i + 1, j)
            if j-1 >= 0:
                func(mat, n, m, visited, i, j - 1)
            if j+1 < m:
                func(mat, n, m, visited, i, j + 1)
            if i-1 >= 0 and j-1 >= 0:
                func(mat, n, m, visited, i - 1, j - 1)
            if i - 1 >= 0 and j + 1 < m:
                func(mat, n, m, visited, i - 1, j + 1)
            if i + 1 < n and j - 1 >= 0:
                func(mat, n, m, visited, i + 1, j - 1)
            if i + 1 < n and j + 1 < m:
                func(mat, n, m, visited, i + 1, j + 1)
            a += 1
        return a

    for i in range(n):
        for j in range(m):
            ans += func(mat, n, m, visited, i, j)

    return ans

n, m = (int(i) for i in input().split())
mat = []
for _ in range(n):
    mat.append([i for i in input().split()])
print(solve(mat, n, m))
