"""1.三个同样的字母连在一起，一定是拼写错误，去掉一个就好啦，比如 helllo -> hello
2.两队一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的第一个字母就好啦，比如helloo -> hello
3.上面的规则优先“从左到右”匹配，即如果是AABBCC，应该优先考虑修复AABB，结果为AABCC
输入：hello 和 wooooooow
输出：hello 和 woow
"""


def func(line, index):
    if (index >= 2) & (line[index] == line[index - 1]) & (line[index - 1] == line[index - 2]):  # AAA型
        return True
    if (index >= 3) & (line[index] == line[index - 1]) & (line[index - 2] == line[index - 3]):  # AABB型
        return True
    return False


n = int(input())
for test in range(n):
    line = input()
    index = 0
    while index < len(line):
        if func(line, index):
            line = line[:index] + line[index + 1:]      # str删除index所在位置的元素
        else:
            index += 1
    print(line)
