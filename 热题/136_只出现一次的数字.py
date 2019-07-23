"""给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：     你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1
示例 2:
输入: [4,1,2,1,2]
输出: 4
"""

'''dict.pop (key[,default])
其中，key是必选参数，必须给出，default是可选参数，可以不给出。
如果键值key在字典中存在，删除dict[key]，返回 dict[key]的value值。
否则，如有给出default值则返回default值，如果default值没有给出，就会报出KeyError异常。
pop()方法至少接受一个参数，最多接受两个参数。
dict.popitem()
随机删除字典中的一个键值对，并且返回该键值对，(key,value)形式。
如果字典已经为空，却调用了此方法，就报出KeyError异常。
'''


class Solution(object):
    def singleNumber(self, nums):       # 位操作法：时间复杂度：O(n)，空间复杂度：O(1)
        """
        如果我们对 0 和二进制位做 异或XOR 运算，得到的仍然是这个二进制位:     a⊕0=a
        如果我们对相同的二进制位做 XOR 运算，返回的结果是 0:              a⊕a=0
        XOR 满足交换律和结合律:                                           a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        所以我们只需要将所有的数进行 XOR 操作，得到那个唯一的数字。
                """
        a = 0
        for i in nums:
            a ^= i
        return a

    def singleNumber1(self, nums):       # 哈希表法：时空复杂度：O(n)
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
