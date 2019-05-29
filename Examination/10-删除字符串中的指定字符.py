"""1.三个同样的字母连在一起，一定是拼写错误，去掉一个就好啦，比如 helllo -> hello
2.两队一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的第一个字母就好啦，比如helloo -> hello
3.上面的规则优先“从左到右”匹配，即如果是AABBCC，应该优先考虑修复AABB，结果为AABCC
输入：hello 和 wooooooow
输出：hello 和 woow
"""


# 从左到右，依次遍历字符串
def func(s):
    s = list(s)                     # 将字符串转换成list，可以使用list.pop()
    i = 2
    while i < len(s):               # 【此处不能使用 for循环，要删除元素，while循环】且每次循环前，都要计算是否满足条件，即len(s)的值在变化
        if i >= 2 and s[i] == s[i-1] == s[i-2]:                 # AAA型，注意需要有 i >= 2
            s.pop(i)                # list.pop()
        elif i >= 3 and s[i] == s[i-1] and s[i-2] == s[i-3]:    # AABB型，注意需要有 i >= 3
            s.pop(i)                # s = s[:i] + s[i+1:] 将新建列表（空间）
        else:
            i += 1                  # 或者则 索引前移
    return ''.join(s)               # 列表转换成字符串


n = int(input())
for _ in range(n):
    s = input()
    print(func(s))

