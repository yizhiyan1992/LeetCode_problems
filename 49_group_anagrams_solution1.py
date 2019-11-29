#approach1: categorize by count
# Two strings are anagrams if and only if their character counts (respective number of occurences of each character) are the same
# time complexity: O(kn)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict=defaultdict(list)
        for i in strs:
            value=[0]*26
            for c in i:
                value[ord(c)-ord('a')]+=1
            Dict[tuple(value)].append(i)
        ans=Dict.values()
        return ans
