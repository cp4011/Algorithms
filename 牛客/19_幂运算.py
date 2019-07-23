"""给定两个数R和n，输出R的n次方，其中0.0<R<99.999, 0<n<=25
输入描述:
多组测试用例，请参考例题的输入处理 输入每行一个浮点数 R 其中0.0 < R <99.999， 一个整数 n 其中0 < n <=25
输出描述:
输出R的n次方
示例1
输入  95.123 12           0.1 1
输出
548815620517731830194541.899025343415715973535967221869852721       0.1
"""
# 把浮点型转化为整数（比如95.123转化为95123 ），再做n次方运算95123**12
# 计算最后小数点的位置.123 小数有3位 12次方后 那就是3*12=16位
# 由于最后得到的整数长度可能会小于小数点需要移动的长度所以要加个补零操作
while True:
    try:
        a, b = input().split()
        index = a.index(".")
        a = a[:index] + a[index + 1:]
        length = len(a)
        length_1 = length - index
        a = int(a)
        b = int(b)
        zeros = length_1 * b
        ans = str(a ** b)
        length_2 = len(ans)
        if length_2 <= zeros:
            ans = "0"*(zeros+1-length_2) + ans
        length_3 = len(ans)
        ans = ans[:length_3-zeros] + "." + str(int(ans[length_3-zeros:][::-1]))[::-1]
        print(ans)                      # ans[length_3-zeros:]后面反转两次 是为了出掉小数点后面多余的0（1.21000000）
    except:
        break
