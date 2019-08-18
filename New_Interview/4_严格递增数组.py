"""给定两个数组A和B，其中数组A是几乎严格升序排序的，机会的定义是只需改变其中一个数，即可满足完全升序排序
你的任务是从数组A中找到这个数字，并从数组B中选取一个数将其交替，使得数组A是完全严格升序排序的
（严格升序排序，即不允许相邻两个为相同的数）
请找出数组B中满足要求的最大数字，并输出最终有序的数组。如果不存在就输出NO"""
'''输入第一行为数组A，第二行为数组B；输出共一行，为最终有序的数组，不存在则输出NO
输入：  1 3 7 4 10
        2 1 5 8 9
输出：  1 3 7 9 10
'''

A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.append(float("inf"))              # 技巧：数组A首尾添加两个数，避免处理首尾
A.insert(0, -float("inf"))
index = 1
for i in range(1, len(A)):
    if A[i] <= A[i - 1]:
        index = i
        break

res = -float("inf")
for i in range(len(B)):
    if B[i] < A[index + 1] and B[i] > A[index - 1] and res < B[i]:
        res = B[i]
if res == -float("inf"):
    print("NO")
else:
    A[index] = res
    for e in range(1, len(A) - 1):
        print(A[e], end=" ")





def func(nums, B):
    l, r = -9999999, 9999999
    index1 = -1
    if len(nums) >= 3 and (nums[0] >= nums[1] and nums[1] < nums[2]) or (nums[-1] <= nums[-2] and nums[-2] > nums[-3]):
        if nums[0] >= nums[1] and nums[1] < nums[2]:
            index1 = 0
            r = nums[1]
        if nums[-1] <= nums[-2] and nums[-2] > nums[-3]:
            index1 = -1
            l = nums[-2]
    else:
        for i in range(1, len(nums)-1):
            if nums[i] <= nums[i-1] or nums[i] >= nums[i+1]:
                index1 = i
                l, r = nums[i-1], nums[i+1]
    B.sort()
    n = len(B)
    l1, r1 = 0, n-1
    if l == -9999999:
        l = r - 1
    if r == 9999999:
        nums[index1] = B[-1]
        return nums
    while l1 <= r1:
        mid = (l1+r1) >> 1
        if B[mid] >= r:
            r1 = mid - 1
        elif B[mid] <= l:
            l1 = mid + 1
        else:
            l1 = mid + 1
    nums[index1] = B[r1]
    return nums


nums = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
if not func(nums, B):
    print(" ".join(map(str, func(nums, B))))
