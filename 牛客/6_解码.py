"""题目描述
有一种将字母编码成数字的方式：'a'->1, 'b->2', ... , 'z->26'。现在给一串数字，给出有多少种可能的译码结果。
输入描述:
编码后数字串
输出描述:
可能的译码结果数
示例1
输入
12
输出
2
说明
2种可能的译码结果（”ab” 或”l”）
示例2
输入
31717126241541717
输出
192
说明
192种可能的译码结果
"""


s=input()
dp=[0]*len(s)
if s[0]!='0': dp[0]=1
for i in range(1, len(s)):
    if s[i] == '0':
        if s[i-1] == '1' or s[i-1]=='2':
            dp[i]=dp[i-2] if i>=2 else 1
    elif s[i]<='6':
        dp[i]=dp[i-1]
        if s[i-1]=='1' or s[i-1]=='2': dp[i]+=(dp[i-2] if i>=2 else 1)
    else:
        dp[i]=dp[i-1]
        if s[i-1]=='1': dp[i]+=(dp[i-2] if i>=2 else 1)
print(dp[-1])


a=input()
memo={}
def main(a):            # 返回a有多少种编码结果
    if a in memo:
        return memo[a]
    if a=='0':
        return 0
    if len(a)==0:
        return 1
    if len(a)==1:
        return 1
    tmp=a[:2]
    hou=a[2:]
    if int(tmp)==10:
        return main(hou)
    if int(tmp)==20:
        return main(hou)
    if int(tmp)<27:
        case1=main(a[1:])
        case2=main(a[2:])
        memo[a]=case1+case2
        return memo[a]
    else:
        case1=main(a[1:])
        memo[a]=case1
        return memo[a]
if a=='0':
    print(0)
else:
    print(main(a))