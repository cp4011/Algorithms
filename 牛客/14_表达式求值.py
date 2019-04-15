"""今天上课，老师教了小易怎么计算加法和乘法，乘法的优先级大于加法，但是如果一个运算加了括号，那么它的优先级是最高的。例如：
1+2*3=7
1*(2+3)=5
1*2*3=6
(1+2)*3=9
现在小易希望你帮他计算给定3个数a，b，c，在它们中间添加"+"， "*"， "("， ")"符号，能够获得的最大值。

输入描述:
一行三个数a，b，c (1 <= a, b, c <= 10)

输出描述:
能够获得的最大值
示例1
输入
1 2 3
输出
9
"""


def summax(alist):
    a, b, c = alist[0], alist[1], alist[2]
    asum = []
    asum.append(a+b*c)
    asum.append(a*(b+c))
    asum.append(a*b*c)
    asum.append((a+b)*c)
    print(max(asum))


alist = list(map(int, input().split(' ')))       # str.split(str="", num=string.count(str)).分隔符,,num--分割次数。默认-1分隔所有
summax(alist)                                    # split()通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
