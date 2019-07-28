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
    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        t = self.d
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]            # 字典迭代
        t['end'] = True         # 标记单词终点

    def search(self, word: str) -> bool:
        t = self.d
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return 'end' in t

    def startsWith(self, prefix: str) -> bool:
        t = self.d
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True