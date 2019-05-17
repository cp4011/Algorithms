"""给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
"""
'''          left_part          |        right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
需满足：    1. len(left_part)=len(right_part)
            2. max(left_part)<=min(right_part)
将{A,B}中的所有元素划分为相同长度的两个部分，且其中一部分中的元素总是大于另一部分中的元素。median= max(left_part)+min(right_part) / 2
            
只需满足：  1. i+j=m−i+n−j（或：m - i + n - j + 1m−i+n−j+1） 如果 n≥m，只需要使 i=0∼m, j= (m+n+1) / 2 - i
            2. B[j−1]≤A[i] 以及A[i−1]≤B[j]
            
j= (m+n+1) / 2 - i， +1目的是在m+n是奇数时 将中位数放在左边，有return maxLeft，中位数放到左边可以顺利返回，
而放到右边会发生什么？这行代码需要换为return minRight = min(A[i],B[j])，但是i和j并不是始终都会在合法范围内，
以{}{1}为例，一定不能出现A[i]。综上，加一是为了防止数组越界。

时间复杂度：O(log(min(m,n)))，
首先，查找的区间是[0,m]。 而该区间的长度在每次循环之后都会减少为原来的一半。 所以，我们只需要执行log(m) 次循环。
由于m≤n，所以时间复杂度是 O(log(min(m,n)))。
'''


def median(A, B):
    m, n = len(A), len(B)
    if m > n:                       # 使得n≥m，这样j= (m+n+1) / 2 - i，确保j不是负数
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            imin = i + 1                # A[i]小了，下标i右移增大（j相应就减少）,以使B[j-1] <= A[i]
        elif i > 0 and A[i-1] > B[j]:
            imax = i - 1                # A[i-1]太大了，减小i左移，j后移 以使 A[i-1] <= B[j]
        else:                           # i是完美的，即满足 B[j−1]≤A[i] 以及A[i−1]≤B[j]
            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:        # 当m+n为奇数：中位数为 max(A[i−1],B[j−1])
                return max_of_left

            if i == m: min_of_right = B[j]      # m+n为偶数时：中位数是 max(A[i−1],B[j−1])+min(A[i],B[j]) / 2​
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0
