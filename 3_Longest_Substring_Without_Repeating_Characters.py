#deque+set
#time complexity: O(n)
from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        window=deque([])
        window_set=set()
        res=0
        for i in s:
            if i not in window_set:
                window.append(i)
                window_set.add(i)
                if len(window)>res:
                    res=len(window)
            else:
                while i in window_set:
                    last=window.popleft()
                    window_set.remove(last)
                window.append(i)
                window_set.add(i)
        return res
