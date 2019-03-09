from matplotlib import pyplot as plt
plt.subplot(211)                              # 生成几行几列的子图矩阵+子图的位置
plt.plot([1, 2], [1, 4])                      # 参数：plot(X, Y)  X可为数组
plt.subplot(212)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.plot([5, 6, 7, 8], [7, 3, 8, 3])        # 线把点串起来的
# plt.scatter([5, 6, 7, 8], [7, 3, 8, 3])     # 散点图
plt.show()
