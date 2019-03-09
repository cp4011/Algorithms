import matplotlib.pyplot as plt
import PCA

dataMat = PCA.loadDataSet('testSet.txt')
lowDMat, reconMat = PCA.PCA(dataMat, 1)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataMat[:, 0].tolist(), dataMat[:, 1].tolist(), marker='^', s=90)
ax.scatter(reconMat[:, 0].tolist(), reconMat[:, 1].tolist(), marker='o', s=50, c='red')
plt.show()
