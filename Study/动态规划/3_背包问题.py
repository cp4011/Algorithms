"""有n个质量为w1, w2, ..., wn、价值为v1, v2, ..., vn的物品和一个承重为W的背包，如何让背包里装入的物品具有最大价值总和的物品子集
"""
"""动态规划与分治法类似，都是把大问题拆分成小问题，通过寻找大问题与小问题的递推关系，解决一个个小问题，最终达到解决原问题
的效果。但不同的是，分治法在子问题和子子问题等上被重复计算了很多次，而动态规划则具有记忆性，通过填写表把所有已经解决的
子问题答案纪录下来，在新问题里需要用到的子问题可以直接提取，避免了重复计算，从而节约了时间，所以在问题满足最优性原理之后，
用动态规划解决问题的核心就在于填表，表填写完毕，最优解也就找到。
"""
"""寻找递推关系式，面对当前商品有两种可能性：
　　　　第一，包的容量比该商品体积小，装不下，此时的价值与前i-1个的价值是一样的，即V(i,j)=V(i-1,j)；
　　　　第二，还有足够的容量可以装该商品，但装了也不一定达到当前最优价值，所以在装与不装之间选择最优的一个，
                    即V(i,j)=max｛ V(i-1,j)，V(i-1,j-w(i))+v(i) ｝
　　　　　　　其中V(i-1,j)表示不装，V(i-1,j-w(i))+v(i) 表示装了第i个商品，背包容量减少w(i)但价值增加了v(i)；
　　　　由此可以得出递推关系式：
　　　　1) j<w(i)      V(i,j)=V(i-1,j)
　　　　2) j>=w(i)     V(i,j)=max｛ V(i-1,j)，V(i-1,j-w(i))+v(i) ｝
　　填表，首先初始化边界条件，V(0,j)=V(i,0)=0；
    然后一行一行的填表，
　　　　1) 如，i=1，j=1，w(1)=2，v(1)=3，有j<w(1)，故V(1,1)=V(1-1,1)=0；
　　　　2) 又如i=1，j=2，w(1)=2，v(1)=3，有j=w(1),故V(1,2)=max｛ V(1-1,2)，V(1-1,2-w(1))+v(1) ｝=max｛0，0+3｝=3；
　　　　3) 如此下去，填到最后一个，i=4，j=8，w(4)=5，v(4)=6，有j>w(4)，故V(4,8)=max｛ V(4-1,8)，V(4-1,8-w(4))+v(4) ｝=
                    max｛9，4+6｝=10；所以填完表如下图
 
 表格填完，最优解即是V(number,capacity)=V(4,8)=10，但还不知道解由哪些商品组成，故要根据最优解回溯找出解的组成，
 根据填表的原理可以有如下的寻解方式：
　　　　1) V(i,j)=V(i-1,j)时，说明没有选择第i 个商品，则回到V(i-1,j)；
　　　　2) V(i,j)=V(i-1,j-w(i))+v(i)实时，说明装了第i个商品，该商品是最优解组成的一部分，随后我们得回到装该商品之前，即回到V(i-1,j-w(i))；
　　　　3) 一直遍历到i＝0结束为止，所有解的组成都会找到。
    例子：
　　　　1) 最优解为V(4,8)=10，而V(4,8)!=V(3,8)却有V(4,8)=V(3,8-w(4))+v(4)=V(3,3)+6=4+6=10，所以第4件商品被选中，并且回到V(3,8-w(4))=V(3,3)；
　　　　2) 有V(3,3)=V(2,3)=4，所以第3件商品没被选择，回到V(2,3)；
　　　　3) 而V(2,3)!=V(1,3)却有V(2,3)=V(1,3-w(2))+v(2)=V(1,0)+4=0+4=4，所以第2件商品被选中，并且回到V(1,3-w(2))=V(1,0)；
　　　　4) 有V(1,0)=V(0,0)=0，所以第1件商品没被选择；
"""


def bag(n, c, w, v):
    """
    n = 6  物品的数量，
    c = 10 书包能承受的重量，
    w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]    # 二维表格初始化并置零，表示初始状态
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if j < w[i - 1]:
                value[i][j] = value[i - 1][j]
            else:                                               # j >= w[i - 1]： 背包总容量够放当前物体，遍历前一个状态考虑是否置换
                value[i][j] = max(value[i - 1][j], value[i - 1][j - w[i - 1]] + v[i - 1])
    for x in value:
        print(x)
    print('最大价值为:', value[n][c])
    return value


# 优化空间复杂度：O(cn)可以优化为O(c)。二维表格变成一维数组。思路：尾部迭代，每个状态表示上一次的最佳结果。以上时间复杂度为O(cn).已不能再优化了。
def bag1(n, c, w, v):                       # 【缺点：不能回溯找到最优解的组成】，因为只用了以为数组，之前的数据已经被覆盖了
    values = [0 for i in range(c+1)]
    for i in range(1, n + 1):
        for j in range(c, 0, -1):           # 当使用优化空间为O(c)的bag1函数，必须使用逆序遍历。先修改后面的数据再修改前面的数据
            if j >= w[i-1]:                 # 背包总容量够放当前物体，遍历前一个状态考虑是否置换【而j < w[i - 1]和上一行的结果保持不变】
                values[j] = max(values[j], values[j-w[i-1]]+v[i-1])
    return values


# 最优解回溯：输出背包里所放的物品，只需从尾【逆序遍历】物品，当value大于上一行同样位置的value时，表示放进该物品
def show(n, c, w, value):
    print('最大价值为:', value[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):                   # i属于 [n, 1]
        if value[i][j] > value[i - 1][j]:       # 当value大于上一行同样位置的value时，表示第i个物品被放进去了
            x[i - 1] = True                     # 将第i个位置置为True，即下标为i-1
            j -= w[i - 1]
    print('背包中所装物品为:')
    for i in range(n):
        if x[i]:
            print('第', i+1, '个,', end='')


if __name__ == '__main__':
    n = 6
    c = 10
    w = [2, 2, 3, 1, 5, 2]
    v = [2, 3, 1, 5, 4, 3]
    value = bag(n, c, w, v)
    show(n, c, w, value)
    print('\n空间复杂度优化为N(c)结果:', bag1(n, c, w, v))


