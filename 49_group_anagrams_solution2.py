#approach2: categorize by sorted string
# Two strings are anagrams if ond only if their sorted strings are equal
#time complexity: O(nklogk)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict={}
        for i in strs:
            x=sorted(list(i))
            Dict.setdefualt(str(x),[]).append(i)
        ans=list(Dict.values())
        return ans
