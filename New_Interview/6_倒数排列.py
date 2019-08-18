"""把1到n的所有排列按照字典序排成一排，小易从中选出一个排列，假设它是整数第Q个排列，小易希望你能回答他倒数第Q个排列是什么
如 1到3的所有排列是  1 2 3， 1 3 2， 2 1 3， 2 3 1， 3 1 2， 3 2 1 若小易选出的排列是1 2 3，则Q=1，你应该输出排列 3 2 1
输入：3 1 5 2 4    输出：3 5 1 4 2        【相加=6,即n+1】
"""


"""思路： 选出的排列是1 2 3，应该输出排列 3 2 1，每个位置上相加都是 4，即 n+1;
 则直接输出 n+1 - arr[i]"""

# 超出内存
def func(n, arr):
    from itertools import permutations
    nums = list(permutations(list(range(1, n+1))))
    Q = -1
    for i in range(len(nums)):
        if arr == nums[i]:
            Q = i
            break
    res = nums[-Q-1]
    res = list(map(str, res))
    return ' '.join(res)


n = int(input())
arr = (int(i) for i in input().split())
print((func(n, arr)))
