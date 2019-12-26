# Trie+backtracking
# Note that, we backtrack the strings, we need to exclude the boolean value in the dict!
#class Trie:
#    def __init__(self):
#        self.root={}

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root={}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur_level=self.root
        for i in range(len(word)):
            cur_level.setdefault(word[i],{})
            cur_level=cur_level[word[i]]
            if i==len(word)-1:
                cur_level['True']=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        A=word
        word=list(reversed(list(word)))

        def helper(word,trie_level,res):
            if trie_level=={}:
                return False
            if not word:
                if 'True' in trie_level:
                    return True
                return False
            cur_dig=word.pop()

            if cur_dig=='.':
                for i in trie_level.keys():
                    if i!='True':
                        if helper(word,trie_level[i],res):
                            return True
            else:
                if cur_dig in trie_level:
                    if helper(word,trie_level[cur_dig],res):
                        return True
            word.append(cur_dig)
            return res
        return helper(word,self.root,False)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
