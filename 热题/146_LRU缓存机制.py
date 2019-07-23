"""运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前
删除最近最少使用的数据值，从而为新的数据值留出空间。
进阶: 你是否可以在 O(1) 时间复杂度内完成这两种操作？
示例:
LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
"""

# LRU 缓存机制（官方）      有一种叫做有序字典的数据结构，综合了哈希表和链表，在 Python 中为 OrderedDict
from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)       # move_to_end(指定一个key，把对应的key-value移到最后)
        self[key] = value
        if len(self) > self.capacity:   # 当缓存容量达到上限时，应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间
            self.popitem(last=False)    # popitem(默认last=False，按照后进先出原则，删除最后加入的元素，返回key-value)，
                                        # last为False时，它从OrderedDict中删除第一个键值对并返回该键值对
                                        # pop(获取指定key的value，并在字典中删除)    k = dic.pop('key2')

# LRUCache 对象会以如下语句构造和调用:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
