'''非递归归并排序
Description
合并（归并）排序的核心思想是：每次从中间位置将数组分组再分别排序。请实现其非递归方案。
Input
输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。
Output
输出的每一行为排序结果，用空格隔开，末尾不要空格。
Sample Input 1
13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1
3 3 9 12 24 29 34 49 51 56 78 84 100
'''


try:
    while True:
        # 归并排序（递归）
        def merge_sort(li):
            if len(li) == 1:  # 不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
                return li
            mid = len(li) // 2  # 取拆分的中间位置
            left = li[:mid]  # 拆分过后左右两侧子串
            right = li[mid:]
            # 对拆分过后的左右再拆分 一直到只有一个元素为止
            # 最后一次递归时候ll和lr都会接到一个元素的列表
            # 最后一次递归之前的ll和rl会接收到排好序的子序列
            ll = merge_sort(left)
            rl = merge_sort(right)
            # 我们对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表.这里我们调用拎一个函数帮助我们按顺序合并ll和lr
            return merge(ll, rl)

        # 这里接收两个列表
        def merge(left, right):
            # 从两个有顺序的列表里边依次取数据比较后放入result.每次我们分别拿出两个列表中最小的数比较，把较小的放入result
            result = []
            while len(left) > 0 and len(right) > 0:
                if left[0] <= right[0]:  # 为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            result += left  # while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
            result += right
            return result


        c = [int(i) for i in input().split()]
        length = c[0]
        array = merge_sort(c[1:])
        for i in range(length):
            if i == length-1:
                print(array[i])
            else:
                print(array[i], end=" ")
except EOFError:
    pass





