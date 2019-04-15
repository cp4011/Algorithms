"""一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。"""

'''因为n级台阶，第一步有n种跳法：跳1级、跳2级、到跳n级
跳1级，剩下n-1级，则剩下跳法是f(n-1)
跳2级，剩下n-2级，则剩下跳法是f(n-2)
所以f(n)=f(n-1)+f(n-2)+...+f(1)
因为f(n-1)=f(n-2)+f(n-3)+...+f(1)
所以f(n)=2*f(n-1)
'''
'''总得跳法为：

            | 1       ,(n=0 ) 

f(n) =      | 1       ,(n=1 )

            | 2*f(n-1),(n>=2)
'''
class Solution:
    def jumpFloorII(self, number):
        # if number <= 0:
        #     return 0
        # else:
        #     return pow(2, number-1)
        if number == 0:
            return 0
        if number == 1:
            return 1
        ans = 1
        for i in range(2, number+1):
            ans *= 2
        return ans