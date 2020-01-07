'''
Trie
Create a Trie to put all words in.
Search each word in the sentence:
create a var temp to store substring from root to current node, and if there is '1' in root, break searching and return temp (because we need to find the shortest root)
Time complexity: O(n)
'''
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        Trie={}
        for word in dict:
            node=Trie
            for char in word:
                node.setdefault(char,{})
                node=node[char]
            node['1']=True
        sen_lis=sentence.split(' ')
        for i,word in enumerate(sen_lis):
            temp=''
            index=0
            node=Trie
            while index<len(word) and word[index] in node:
                temp+=word[index]
                node=node[word[index]]
                index+=1
                if '1' in node:
                    sen_lis[i]=temp
                    break
        return ' '.join(sen_lis)
