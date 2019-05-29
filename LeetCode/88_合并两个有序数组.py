"""给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
"""


def merge(nums1, m, nums2, n):
    l1, l2, end = m-1, n-1, m+n-1       # 从两数组 nums1和nums2的最后开始比较，填入end位置
    while l1 >= 0 and l2 >= 0:
        if nums2[l2] > nums1[l1]:
            nums1[end] = nums2[l2]
            l2 -= 1
        else:
            nums1[end] = nums1[l1]
            l1 -= 1
        end -= 1            # 每一轮 end 都需要左移1位
    if l1 < 0:          # 若nums2数组还有剩余元素没有处理
        nums1[:l2+1] = nums2[:l2+1]
