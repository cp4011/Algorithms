'''Searching_2
Description
Find the count of numbers less than N having exactly 9 divisors
1<=T<=1000,1<=N<=10^12
Input
First Line of Input contains the number of testcases. Only Line of each testcase contains the number of members N in the rival gang.
Output
Print the desired output.
Sample Input 1
2
40
5
Sample Output 1
1
0
'''


import math


def count_9(N):
    result = 0
    for i in range(1, N):
        count = 0
        k = math.sqrt(i)
        end = math.floor(k) + 1
        for j in range(1, end):
            if i % j == 0:
                count += 2
        if k * k == i:
            count -= 1
        if count == 9:
           #print(i)
            result += 1
    return result


c = int(input())
for i in range(c):
    N = int(input())
    print(count_9(N))





#C++版本
# #include<vector>
# #include<math.h>
# #include<iostream>
# using namespace std;
#
# int solution(int l)
# {
#     int lim=sqrt(l);
#     vector<int> a(lim-2);
#     for(int i=0; i<lim-2; i++)
#     {
#         if(a[i]==0)
#         {
#             int j=i+2;
#             for(int k=2; (k*j)<lim; k++)
#             {
#                 a[(k*j)-2]=1;
#             }
#         }
#     }
#
#     int c=0;
#     for(int i=0; i<lim-2; i++)
#     {
#         if(a[i]==0)
#         {
#
#             if(pow(i+2,8)<=l)
#             {
#                 c++;
#             }
#             for(int j=i+1; j<lim-2; j++)
#             {
#                 if(a[j]==0)
#                 {
#                     if(pow((i+2)*(j+2),2)<=l)
#                     {
#                         c++;
#                     }
#                     else
#                     {
#                         break;
#                     }
#                 }
#             }
#         }
#     }
#     return c;
# }
#
# int main()
#  {
# 	int t;
# 	cin>>t;
# 	while(t--){
# 	    int n;
# 	    cin>>n;
# 	    cout<<solution(n)<<endl;
# 	}
# 	return 0;
# }