class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)
        word_dict = {}
        for word in word_set:
            for index in range(len(word)):
                new_word = word[:index]+"_"+word[index+1:]
                if new_word not in word_dict.keys():
                    word_dict[new_word] = [word]
                else:
                    word_dict[new_word].append(word)
        cur_word = [beginWord]
        next_word = []
        depth = 1
        while cur_word:
            for word in cur_word:
                if word == endWord:
                    return depth
                for index in range(len(word)):
                    new_word = word[:index]+"_"+word[index+1:]
                    if new_word in word_dict.keys():
                        for w in word_dict[new_word]:
                            if w not in next_word:
                                next_word.append(w)
                        del word_dict[new_word]
            depth += 1
            cur_word = next_word
            next_word = []
        return 0

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    sequence_length = Solution().ladderLength(beginWord, endWord, wordList)
    print(sequence_length)
