"""两人共同编写的一个程序来决定奖金的归属。每次获奖后，这个程序首先会随机产生若干0~1之间的实数{p_1, p_2, …, p_n}，然后
从小明开始，第一轮以p_1的概率将奖金全部分配给小明，第二轮以p_2的概率将奖金全部分配给小华，这样交替地小明、小华以p_i的
概率获得奖金的全部，一旦奖金被分配，则程序终止，如果n轮之后奖金依旧没发出，则从p_1开始继续重复（这里需要注意，如果n是奇数，
则第二次从p_1开始的时候，这一轮是以p_1的概率分配给小华）；直到100轮，如果奖金还未被分配，程序终止，两人约定通过支付宝将奖金捐出去。
"""
"""in:
输入数据包含N+1行，
第一行包含一个整数N
接下来N行，每行一个0~1之间的实数，从p_1到p_N
out:
单独一行，输出一个小数，表示小明最终获得奖金的概率，结果四舍五入，小数点后严格保留4位(这里需要注意，如果结果为0.5，则输出0.5000)。
in example:
1
0.999999
out example:
1.0000
"""

import sys
n = int(sys.stdin.readline().strip())
probs = list()
for i in range(n):
    probs.append(float(sys.stdin.readline().strip()))
p_ming = 0
p_hua = 0
p_current = 1
for i in range(100):
    if i % 2 == 0:
        p_ming += p_current*probs[i % len(probs)]
        p_current *= (1-probs[i % len(probs)])
    else:
        p_hua += p_current*probs[i % len(probs)]
        p_current *= (1 - probs[i % len(probs)])
s = str(round(p_ming, 4))                       # round( x [, n]  ) x四舍五入，默认值为 0。 x -- 数字表达式。n-表示从小数点位数
s = s + '0'*(4-len(s.split('.')[1]))
print(s)


