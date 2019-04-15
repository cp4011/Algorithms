"""题目描述
如果一个01串任意两个相邻位置的字符都是不一样的,我们就叫这个01串为交错01串。例如: "1","10101","0101010"都是交错01串。
小易现在有一个01串s,小易想找出一个最长的连续子串,并且这个子串是一个交错01串。小易需要你帮帮忙求出最长的这样的子串的长度是多少。
输入描述:
输入包括字符串s,s的长度length(1 ≤ length ≤ 50),字符串中只包含'0'和'1'
输出描述:
输出一个整数,表示最长的满足要求的子串长度。
示例1
输入
111101111
输出
3
"""

a = input()                                 # '111101111'

if len(a) == 0:
    print(0)
elif len(a) == 1:
    print(1)
elif len(a) == 2:
    if a[0] == a[1]:
        print(2)
    else:
        print(1)
else:
    count = 1
    res = []                                # <class 'list'>: [1, 1, 1, 2, 3, 1, 1, 1]
    for i in range(0, len(a) - 1):
        if a[i] != a[i + 1]:
            count += 1
            res.append(count)
        else:
            res.append(1)
            count = 1
    max = max(res)
    print(max)
