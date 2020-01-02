'''
Maze+BFS
since each word can only be replaced by one letter, the edit distance is just 1.
To find the unweighted shortest distance, we can use BFS.
To build the adj list is time consuming for this problem. Instead, we can think it as a maze problem which has 26 directions for each letter.
, and remove the visited node from set.
'''
from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList) :
        if endWord not in wordList: return 0
        Set=set(wordList)
        Set.add(beginWord)
        def BFS(beginWord,endWord):
            stack = deque([])
            stack.append(endWord)
            Set.remove(endWord)
            layer=0
            while stack:
                for _ in range(len(stack)):
                    node = stack.popleft()
                    for i in range(len(node)):
                        for j in range(26):
                            if node[:i]+chr(97+j)+node[i+1:] in Set:
                                stack.append(node[:i]+chr(97+j)+node[i+1:])
                                Set.remove(node[:i]+chr(97+j)+node[i+1:])
                layer+=1
                print(stack)
                if beginWord in stack: return layer+1
            return 0
        return BFS(beginWord,endWord)
