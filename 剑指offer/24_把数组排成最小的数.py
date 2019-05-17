"""输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。
"""

'''      * 先将整型数组转换成String数组，然后将String数组排序，最后将排好序的字符串数组拼接出来。关键就是制定排序规则。
         * 排序规则如下：          
                若a＋b<b+a  a排在前
                若a＋b>b+a  b排在前
         * 解释说明：比如 a"3", b"31"      a+b"331" > b+a"313"，所以要将二者拼接起来进行比较,结果是b在a前面
 '''


def fun(numbers):
    import functools        # python 3中的 sorted( ) 除去的cmp 参数，推荐使用 key。Python中有相应的函数 支持将 cmp函数转化为key的值。

    num = list(map(str, numbers))
    tcmp = lambda x, y: int(x+y) - int(y+x)         # :后的表达式 即为整个lambda匿名函数的返回值
    num.sort(key=functools.cmp_to_key(tcmp))        # functools.cmp_to_key() 将 cmp函数 转化为 key,cmp函数的返回值 必须为 [1,-1,0]

    return ''.join(num)


print(fun([3, 32, 321]))

