"""如果version1 > version2 返回1，如果 version1 < version2 返回-1，不然返回0.
输入的version字符串非空，只包含数字和字符.。.字符不代表通常意义上的小数点，只是用来区分数字序列。例如字符串2.5并不代表二点五，
只是代表版本是第一级版本号是2，第二级版本号是5.
"""
# 85% 缺少 非等长度判断
a1, a2 = input().split()
if a1 == a2:
    print("0")
else:
    arr1 = [int(i) for i in a1.split(".")]
    arr2 = [int(i) for i in a2.split(".")]
    n = min(len(arr1), len(arr2))
    for i in range(n):
        if arr1[i] == arr2[i]:
            continue
        elif arr1[i] > arr2[i]:
            print("1")
            break               # 提前break时，i的值会暂停那一时刻，因此接下来可以 根据i的值来判断是否是正常结束循环还是提前break的
        else:
            print("-1")
            break


# 改正
def judgeTwoVersion(str0):
    a, b = str0[0], str0[1]
    list_a, list_b = a.split('.'), b.split('.')
    mylen = min(len(list_a), len(list_b))
    # 等长度判断
    for i in range(mylen):
        if int(list_a[i]) < int(list_b[i]):
            print('-1')
            break
        elif int(list_a[i]) > int(list_b[i]):
            print('1')
            break
        elif int(list_a[i]) == int(list_b[i]):
            continue
    # 非等长度判断
    if i == mylen - 1 and list_a[mylen - 1] == list_b[mylen - 1]:       # 注意此时的i是全局变量，用作条件判断
        if len(list_a) > len(list_b):
            print('1')
        elif len(list_a) < len(list_b):
            print('-1')
        elif len(list_a) == len(list_b):
            print('0')


if __name__ == '__main__':
    str0 = [i for i in input().split()]  # 输入字符串
    judgeTwoVersion(str0)   # 输出判断结果
