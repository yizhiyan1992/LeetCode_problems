'''
Greedy solution: time complexity O(n)
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        Dict={}
        for index,char in enumerate(S):
            Dict[char]=index
        start=0;end=0
        res=[]
        for index,char in enumerate(S):
            if Dict[char]>end:
                end=Dict[char]
            if index==end:
                res.append(end-start+1)
                start=end+1
                end=end+1
        return res
