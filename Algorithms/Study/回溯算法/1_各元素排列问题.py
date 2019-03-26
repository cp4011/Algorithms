class Solution:
    def solvePermutation(self, array, n):
        self.helper(array, n, [])				# 调用helper方法启动，第一次调用，传入的排序列表solution为空

    def helper(self, array, n, solution):
        if len(solution) == n:				    # 如果没有剩余排序对象【helper方法的返回条件】
            print(solution)					    # 输出结果
            return						        # 返回上一次被调用的地方
        for i in range(len(array)):					        # 第一本书的选择
            newSolution = solution + [array[i]]		        # 加入书本
            newArray = array[:i] + array[i+1:]			    # 删除书本[组合问题时：newArray = array[i + 1:]】
            self.helper(newArray, n, newSolution)		    # 寻找剩余对象的排序集合


Solution().solvePermutation(["红", "黄", "蓝", "绿"], 2)    # 排列问题 A 4 2 = 12种
