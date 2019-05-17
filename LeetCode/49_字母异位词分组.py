"""给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明： 所有输入均为小写字母。 不考虑答案输出的顺序。
"""

''' 排序数组分类
当且仅当它们的排序字符串相等时，两个字符串是字母异位词。
维护一个映射 ans : {String -> List}，其中每个键 K 是一个排序字符串，每个值是初始输入的字符串列表。
在 Java 中，我们将键存储为字符串。 在 Python 中，我们将键存储为散列化元组，例如，('c', 'o', 'd', 'e')。
'''


class Solution(object):
    def groupAnagrams(self, strs):
        import collections
        ans = collections.defaultdict(list)     # list.append()
        for s in strs:
            ans[str(sorted(s))].append(s)   # sorted()返回的是list列表，不能作为键 被hash。可以转成字符串str()或者元组tuple()
        return list(ans.values())           # 必须list()转化，实现dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
