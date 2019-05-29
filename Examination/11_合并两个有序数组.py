"""合并两个有序数组"""


def merge(list1, list2):
    result = []
    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1[0])
            list1.pop(0)            # list.pop()
        else:
            result.append(list2[0])
            del list2[0]            # del 元素
    if list1:
        result.extend(list1)
    if list2:
        result.extend(list2)
    return result


arr1 = [int(i) for i in input().strip().split()]
arr2 = [int(i) for i in input().strip().split()]
print(merge(arr1, arr2))
