def func(arr, n):
    ans = -10000
    for i in range(n):
        for j in range(i+1,n):
            ans = max(ans, arr[i]+arr[j]+i-j)
    return ans

n = int(input())
arr = [int(i) for i in input().split()]
print(func(arr, n))


"""超时 30%

5
11 6 5 18 12

输出：29"""