class Solution:
    def solvePermutation(self, array, n):
        list = []
        self.helper(array, n, [], list)         # 调用helper方法启动，第一次调用，传入的排序列表solution为空
        return list

    def helper(self, array, n, solution, list):
        if len(solution) == n:				    # 如果没有剩余排序对象【helper方法的返回条件】
            # print(solution)					# 输出结果
            list.append(solution)
            return						        # 返回上一次被调用的地方
        for i in range(len(array)):					        # 第一本书的选择
            newSolution = solution + [array[i]]		        # 加入书本
            newArray = array[:i] + array[i+1:]			    # 删除书本[组合问题时：newArray = array[i + 1:]】
            self.helper(newArray, n, newSolution, list)		# 寻找剩余对象的排序集合


print(Solution().solvePermutation(["红", "黄", "蓝", "绿"], 2))    # 排列问题 A 4 2 = 12种


# 用python实现排列组合C(n,m) = n!/(n-m)!
def get_value(n):
    if n == 1:
        return n
    else:
        return n * get_value(n - 1)


def gen_last_value(n, m):
    first = get_value(n)
    second = get_value((n - m))
    return first / second


# if __name__ == "__main__":
#     rest = gen_last_value(4, 2)         # A(4, 2)
#     print("value:", rest)


# for循环遍历
num_list = [1, 2, 3]
result = []
for i in num_list:
      for j in num_list:
            for k in num_list:
                  if len(set((i, j, k))) == 3:          # 去重后长度仍为3的话说明i,j,k的值都不相同
                         result.append(list((i, j, k)))
# print(result)
