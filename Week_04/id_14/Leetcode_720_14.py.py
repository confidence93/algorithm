class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
    
    def longest_word(self):
        def helper(node, partial_res):
            res = partial_res
            for c, child in node.children.items():
                if child.end:
                    pot = helper(child, partial_res + c)
                    if len(pot) > len(res):
                        res = pot
                    elif len(pot) == len(res) and pot < res:
                        res = pot
            return res
        return helper(self.root, '')

class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        T = Trie()
        for word in words:
            T.insert(word)
        return T.longest_word()


½â·¨¶þ:
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        words_set, longest_word = set(['']), ''
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word