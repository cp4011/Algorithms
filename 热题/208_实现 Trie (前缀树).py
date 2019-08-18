"""实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
示例:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:
你可以假设所有的输入都是由小写字母 a-z 构成的。  保证所有输入均为非空字符串。
"""


class Trie:
    def __init__(self):     # 用dict模拟字典树即可
        """        Initialize your data structure here.        """
        self.root = {}

    def insert(self, word):  # Trie树的每个节点本身不存储字符，是整个树的路径信息存储字符,
        """  Inserts a word into the trie.        :type word: str        :rtype: None        """
        node = self.root
        for char in word:   # Python 字典 setdefault() 方法和 [get()方法]类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值
            node = node.setdefault(char, {})  # 如果key在字典中,返回对应的值;如果不在字典中，则插入key及设置的默认值default并返回default,default默认值为None

        node["end"] = True  # 有些节点存储"end"标记位：则标识从根节点root到当前node节点的路径构成一个单词

    def search(self, word):
        """        Returns if the word is in the trie.        :type word: str        :rtype: bool        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]

        return "end" in node

    def startsWith(self, prefix):
        """Returns if there is any word in the trie that starts with the given prefix. :type prefix: str :rtype: bool"""
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
