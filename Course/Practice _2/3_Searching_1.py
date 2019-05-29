'''Searching_1
Description
Dilpreet wants to paint his dog- Buzo's home that has n boards with different lengths[A1, A2,..., An]. He hired k painters for this work and each painter takes 1 unit time to paint 1 unit of the board.The problem is to find the minimum time to get this job done under the constraints that any painter will only paint continuous sections of boards, say board {2, 3, 4} or only board {1} or nothing but not board {2, 4, 5}.
Constraints:1<=T<=100,1<=k<=30,1<=n<=50,1<=A[i]<=500
Input
The first line consists of a single integer T, the number of test cases. For each test case, the first line contains an integer k denoting the number of painters and integer n denoting the number of boards. Next line contains n- space separated integers denoting the size of boards.
Output
For each test case, the output is an integer displaying the minimum time for painting that house.
Sample Input 1
2
2 4
10 10 10 10
2 4
10 20 30 40
Sample Output 1
20
60
'''


def sum(arr, frm, to):
    total = 0
    for i in range(frm, to + 1):
        total += arr[i]
    return total


def findmax(arr, n, k):
    ls_n = [0]*(n+1)
    ls_k = []
    for i in range(k+1):
        temp = ls_n.copy()
        ls_k.append(temp)
    for i in range(1, n+1):
        ls_k[1][i] = sum(arr, 0, i-1)
    for i in range(1, k+1):
        ls_k[i][1] = arr[0]
    for i in range(2, k+1):
        for j in range(2, n+1):
            best = 100000000
            for p in range(1, j+1):
                best = min(best, max(ls_k[i-1][p], sum(arr, p, j-1)))
            ls_k[i][j] = best
    return ls_k[k][n]


count = int(input().strip())
k, n, arr = [], [], []
for i in range(count):
    num_ls = list(map(int, input().strip().split()))
    k.append(num_ls[0])
    n.append(num_ls[1])
    arr.append(list(map(int, input().strip().split())))

for j in range(count):
    print(findmax(arr[j], n[j], k[j]))


#C++版本
# #include <climits>
# #include <iostream>
# using namespace std;
#
#
# int sum(int arr[], int from, int to)
# {
# 	int total = 0;
# 	for (int i = from; i <= to; i++)
# 		total += arr[i];
# 	return total;
# }
#
# int Solution(int arr[], int n, int k)
# {
# 	int dp[k + 1][n + 1] = { 0 };
#
# 	for (int i = 1; i <= n; i++)
# 		dp[1][i] = sum(arr, 0, i - 1);
#
# 	for (int i = 1; i <= k; i++)
# 		dp[i][1] = arr[0];
#
# 	for (int i = 2; i <= k; i++) {
# 		for (int j = 2; j <= n; j++) {
#
# 			int best = INT_MAX;
#
# 			for (int p = 1; p <= j; p++)
# 				best = min(best, max(dp[i - 1][p],
# 							sum(arr, p, j - 1)));
#
# 			dp[i][j] = best;
# 		}
# 	}
#
# 	return dp[k][n];
# }
#
# int main()
# {
#
#     int t;
# 	cin>>t;
# 	while(t--){
# 	  int k,n,i;
# 	  int a[1000];
# 	  cin>>k>>n;
# 	  for(i = 0; i < n; i++)
#       {
#           cin >> a[i];
#       }
# 	  cout<<Solution(a,n,k)<<endl;
# 	}
#
# 	return 0;
# }