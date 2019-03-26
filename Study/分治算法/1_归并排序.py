"""     分治算法：分而治之            归并排序        """


# 归并排序（自顶向下递归法）
def mergeSort(myList):                                          # 传入参数myList
    if len(myList) < 2:                                         # 如果myList只有一个元素，终止
        return
    cut = len(myList) // 2                                      # 找到列表中点
    listA = myList[:cut]                                        # 左子列表
    listB = myList[cut:]                                        # 右子列表
    mergeSort(listA)                                            # 递归 把左子列表归并排序
    mergeSort(listB)                                            # 递归 把右子列表归并排序
    pointerA = 0                                                # 指针A，即列表的下标
    pointerB = 0                                                # 指针B，即列表的下标
    counter = 0                                                 # 定义一个counter
    while pointerA < len(listA) and pointerB < len(listB):      # 如果两个指针都没走到头
        if listA[pointerA] < listB[pointerB]:                   # 比子列表元素大小
            myList[counter] = listA[pointerA]                   # 小的元素替换myList[counter]
            pointerA += 1                                       # 移动指针
        else:
            myList[counter] = listB[pointerB]
            pointerB += 1
        counter += 1                                            # counter加一
    while pointerA < len(listA):                                # 如果指针B走到头了但指针A没有
        myList[counter] = listA[pointerA]                       # 指针A对应的元素替换myList[counter]
        pointerA += 1
        counter += 1
    while pointerB < len(listB):                                # 如果指针A走到头了但指针B没有
        myList[counter] = listB[pointerB]                       # 指针B对应的元素替换myList[counter]
        pointerB += 1
        counter += 1


listX = [2, 3, 4, 1, 3, 0]
mergeSort(listX)
print(listX)


# 递归
def merge_sort(li):
    if len(li) == 1:        # 不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
        return li
    mid = len(li) // 2      # 取拆分的中间位置
    left = li[:mid]         # 拆分过后左右两侧子串
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
        if left[0] <= right[0]:     # 为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left                  # while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    result += right
    return result


# 归并排序（自底向上迭代法）:有问题
def mergeSort(myList):								    # 传入参数myList
    length = len(myList)     							# myList的长度
    n = 1									            # n为子数组长度，初始值为1
    while n < length:							        # 如果子数组长度小于myList的长度
          for i in range(0, length, n*2):					# 利用for loop把子数组成对排序
                listA = myList[i:i+n]						    # listA与listB为一对长度为n的子数组
                listB = myList[i+n:i+n*2]
                pointerA = 0							        # 利用指针将listA与listB排序
                pointerB = 0
                counter = i
                while pointerA < len(listA) and pointerB < len(listB):  # 如果两个指针都没走到头
                    if listA[pointerA] < listB[pointerB]:  # 比子列表元素大小
                        myList[counter] = listA[pointerA]  # 小的元素替换myList[counter]
                        pointerA += 1  # 移动指针
                    else:
                        myList[counter] = listB[pointerB]
                        pointerB += 1
                    counter += 1  # counter加一
                while pointerA < len(listA):  # 如果指针B走到头了但指针A没有
                    myList[counter] = listA[pointerA]  # 指针A对应的元素替换myList[counter]
                    pointerA += 1
                    counter += 1
                while pointerB < len(listB):  # 如果指针A走到头了但指针B没有
                    myList[counter] = listB[pointerB]  # 指针B对应的元素替换myList[counter]
                    pointerB += 1
                    counter += 1
                n = n*2									        # 将n乘2


listX = [-2, 9, 0, 8, 5, -4, 8]
mergeSort(listX)
print(listX)


