"""题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
输入描述:
题目保证输入的数组中没有的相同的数字
    数据范围：
    对于%50的数据,size<=10^4
    对于%75的数据,size<=10^5
    对于%100的数据,size<=2*10^5
示例1
输入
1,2,3,4,5,6,7,0
输出
7
"""


''' 1. 暴力求解法，时间复杂度为o（n^2）,空间复杂度o(1)
        for(int i = 0; i < d.size(); ++i){
            for(int j = 0; j < i; ++j)  if(d[j] > d[i])  ++r;
    2. 使用归并排序的思想进行处理，时间复杂度o(nlog(n)),空间复杂度0（n）
        归并排序走一遍 合并时对于右边的数统计一下左边比他小的个数，此个数即为逆序对个数
'''


class Solution:
    def InversePairs(self, data):
        # 发现可以用归并排序，归并拼接后用计算排序时元素的index变动了多少.两个有序序列，每个元素移动index数,之和好像刚好等于逆序对的个数
        _, s = self.MergeSort(data)
        return s % 1000000007

    def MergeSort(self, data):
        n = len(data)
        if n == 1:
            return data, 0
        part1, part2 = data[:n // 2], data[n // 2:]         # 分两半来排序
        sorted_part1, s1 = self.MergeSort(part1)
        sorted_part2, s2 = self.MergeSort(part2)
        s, sorted_temp = 0, sorted_part1 + sorted_part2      # 排序后拼接这两半，拼接后先计数，然后将两个有序序列合并
        # 用p、q两个指针指向两段，计算q中每个元素离插入点的index差
        p, q, len1, len_all = 0, sorted_temp.index(sorted_part2[0]), len(sorted_part1), len(sorted_temp)
        while p < len1 and q < len_all:
            while p < len1:         # 移动p使p成为插入排序的插入点，计算要移动多少个位置
                if sorted_temp[q] < sorted_temp[p]:
                    s += len1 - p
                    break
                p += 1
            q += 1
        # 完成排序，并把排序后的内容回溯给上一级做准备
        l = []
        p, q = 0, sorted_temp.index(sorted_part2[0])
        while p < len1 and q < len_all:
            if sorted_temp[p] < sorted_temp[q]:
                l.append(sorted_temp[p])
                p += 1
            else:
                l.append(sorted_temp[q])
                q += 1
        if p == len1:
            l += sorted_temp[q:]
        if q == len_all:
            l += sorted_part1[p:]
        return l, s + s1 + s2


class Solution1:
    def InversePairs(self, data):
        # write code here
        def mergeSort(temp, l, r, data):
            if l >= r:
                temp[l] = data[l]
                return 0
            mid = (l + r) / 2
            left = mergeSort(data, l, mid, temp)
            right = mergeSort(data, mid + 1, r, temp)

            count = 0
            i, j = l, mid + 1
            ind = l
            while i <= mid and j <= r:
                if data[i] > data[j]:
                    temp[ind] = data[j]
                    j += 1
                    count += mid + 1 - i
                else:
                    temp[ind] = data[i]
                    i += 1
                ind += 1
            while i <= mid:
                temp[ind] = data[i]
                i += 1
                ind += 1
            while j <= r:
                temp[ind] = data[j]
                j += 1
                ind += 1
            return count + left + right

        return mergeSort(data[:], 0, len(data) - 1, data) % 1000000007


class Solution2:
    def InversePairs(self, data):
        count = 0
        copy = data[:]
        copy.sort()

        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])

        return count % 1000000007


'''输入数组：data=[3,2,1,5,4,6,0,7]
排序好数组：dataSorted=[0,1,2,3,4,5,6,7]
顺序遍历dataSorted数组，第一个元素0是最小的元素，因此在data数组中，0前面有多少个数，就有多少个逆序对。在0检测完之后，
将0从data数组中删除，data=[3,2,1,5,4,6,7]，dataSorted数组遍历到1，而1其实就是[1,2,3,4,5,6,7]中的最小元素
因此，原问题就变为子问题：
输入数组：data=[3,2,1,5,4,6,7]
排序好数组：dataSorted=[1,2,3,4,5,6,7]
……
直到遍历到最后一个元素。
'''