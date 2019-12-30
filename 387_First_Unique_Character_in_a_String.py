# Dict, time complexity: O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        Dict={}
        for i in range(len(s)):
            Dict.setdefault(s[i],[])
            Dict[s[i]].append(i)
        temp=[]
        for i in Dict.values():
            if len(i)==1:
                temp.append(i[0])
        if not temp:
            return -1
        return min(temp)
