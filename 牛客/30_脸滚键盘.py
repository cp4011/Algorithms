"""大小姐脸滚键盘打出的一行字中的第 `k` 个仅出现一次的字。(为简化问题，大小姐没有滚出 ascii 字符集以外的字)
输入描述:
每个输入都有若干行，每行的第一个数字为`k`，表示求第`k`个仅出现一次的字。然后间隔一个半角空格，之后直到行尾的所有字符表示
大小姐滚出的字符串`S`。
输出描述:
输出的每一行对应输入的每一行的答案，如果无解，输出字符串`Myon~`
(请不要输出多余的空行）
为了方便评测，如果答案存在且为c，请输出[c]
输入例子1:
2 misakamikotodaisuki
3 !bakabaka~ bakabaka~ 1~2~9!
3 3.1415926535897932384626433832795028841971693993751o582097494459211451488946419191919l91919hmmhmmahhhhhhhhhh
7 www.bilibili.com/av170001
1 111
输出例子1:
[d]
[9]
[l]
[7]
Myon~
"""


def func(s, k):
    from collections import Counter         # 牛客网支持 字典记数
    d = Counter(s)
    count = 0
    ans = 'Myon~'
    for i in s:
        if d[i] == 1:
            count += 1
        if count == k:
            ans = i
            break
    return ans


while True:                         # 注意 while True 还有try ; except break
    try:
        k, s = input().split(' ', 1)    # 注意只切出第一份k
        ans = func(s, int(k))
        if ans == 'Myon~':          # 注意此处输出是 没有中括号的
             print('Myon~')
        else:
             print("[%s]" % func(s, int(k)))
    except:
        break
