'''字符串1
Description
Given a string ‘str’ of digits, find length of the longest substring of ‘str’, such that the length of the substring
is 2k digits and sum of left k digits is equal to the sum of right k digits.
Input
输入第一行是测试用例的个数，后面每一行表示一个数字组成的字符串，例如："123123"
Output
输出找到的满足要求的最长子串的长度。例如，给定的例子长度应该是 6。每行对应一个用例的结果。
Sample Input 1
1
1538023
Sample Output 1
4
'''


def func(s):
    length = len(s)                                 # length=7
    k_digits = range(1, int(length/2)+1)            # [1,3]
    k_digits = k_digits[::-1]                       # 将k从大到小排列，这样return出来的k一定是最大的
    datas = [int(s[i]) for i in range(len(s))]
    for k in k_digits:                              # k分别 = 3, 2, 1
        for j in range(length-2*k+1):               # 当k=3时，j分别可以取值range(2),即0, 1
            left = sum(datas[j:j+k])
            right = sum(datas[j+k:j+2*k])
            if left == right:
                return k                            # 因为k是从大到小的，因此第一次返回的一定是满足题意最大的k
    return 0


T = int(input())
for i in range(T):
    s = input()
    print(func(s)*2)                                # 2k
