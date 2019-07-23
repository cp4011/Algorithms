"""统计一个数字在排序数组中出现的次数。"""

'''查找有序数组：二分查找'''


class Solution:                 # 统计一个数字在排序数组中出现的次数
    def GetNumberOfK(self, data, k):                        # 查找有序数组：二分查找
        if not data or k < data[0] or k > data[-1]:         # 注意边界
            return 0
        index = -1
        length = len(data)
        l, r = 0, length - 1
        while l <= r:                       # 注意要有=，如测试数据为[3],3.应该输出为1，但是没有=，则输出0
            mid = (l + r) >> 1              # 除于2，用 【右移>>1】. 【注意不是>>2]
            if data[mid] == k:
                index = mid
                break                       # 【注意要break】
            elif data[mid] > k:
                r = mid - 1
            else:
                l = mid + 1
        if index == -1:
            return 0
        count = 1
        low = index - 1
        high = index + 1
        while low >= 0 and data[low] == k:
            count += 1
            low -= 1
        while high < length and data[high] == k:
            count += 1
            high += 1
        return count
