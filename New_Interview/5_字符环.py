"""给定一个字符串数组，所有字符均为大写字母，请问给定的字符串数组是否能通过更换数组中的元素的顺序，从而首尾相连，
形成一个环，换上相邻字符串首尾衔接的字符相同"""
'''输入：CAT TIGER RPC 输出：true
   输入：CAT RPC       输出：false'''


def func(ss):
    s = ss.split()
    n = len(s)              # 重点：构造 数据结构
    arr1, arr2 = [], []  # <class 'list'>: [('C', 'T'), ('T', 'R'), ('R', 'C')] <class 'list'>: [[1, 1], [1, 1], [1, 1]]
    for x in s:
        arr1.append((x[0], x[-1]))
        arr2.append([1, 1])
    for i in range(n):          # 从左到右开始遍历，两两组合
        for j in range(i+1, n):
            if arr2[i][0] == 1 and arr2[j][1] == 1 and arr1[i][0] == arr1[j][1]:
                arr2[i][0] = 0
                arr2[j][1] = 0
            if arr2[i][1] == 1 and arr2[j][0] == 1 and arr1[i][1] == arr1[j][0]:
                arr2[i][1] = 0
                arr2[j][0] = 0
    count = 1
    for k in arr2:
        if k[0] != 0 or k[1] != 0:
            count += 1
    return count == 1


ss = input()
if func(ss):
    print("true")       # 注意 是true，不是True
else:
    print("false")
