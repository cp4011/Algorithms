ans = []
class Solution:
    def solveCombination(self, array, n):
        self.helper(array, n, [])				        # 调用helper方法起始

    def helper(self, array, n, solution):			    # helper方法
        if len(solution) == n:					        # 如果solution中有n门课程
            global ans
            ans.append(solution)
            print(solution)					            # 输出结果
            return							            # 返回被调用的地方
        for i in range(len(array)):					    # for每一个课目选项
            newSolution = solution + [array[i]]		    # 把课程加入到新的组合列表
            newArray = array[i + 1:]					# 创建新课程列表，更新列表【排列问题时：newArray = array[:i] + array[i+1:]】
            self.helper(newArray, n, newSolution)		# 调用helper方法选择剩余课程


Solution().solveCombination(['A', 'B', 'C', 'D'], 2)    # 组合问题 C 4 2 = 6种
print(ans)


# 用python实现排列组合C(n,m) = n!/m!*(n-m)!
def get_value(n):
    if n == 1:
        return n
    else:
        return n * get_value(n - 1)


def gen_last_value(n, m):
    first = get_value(n)
    second = get_value(m)
    third = get_value((n - m))
    return first / (second * third)


# if __name__ == "__main__":
#     rest = gen_last_value(4, 2)         # C(4, 2)
#     print("value:", rest)

