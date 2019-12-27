class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root={}
        self.ending=-1

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_level=self.root
        for i in word:
            cur_level.setdefault(i,{})
            cur_level=cur_level[i]
        cur_level[self.ending]='True'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_level=self.root
        for i in word:
            if i not in cur_level:
                return False
            cur_level=cur_level[i]
        if self.ending in cur_level:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_level=self.root
        for i in prefix:
            if i not in cur_level:
                return False
            cur_level=cur_level[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
