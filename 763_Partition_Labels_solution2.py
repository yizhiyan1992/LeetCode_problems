'''
Merge solution, time complexity O(nlogn)
Use a dict to store the start and the end position of each letter, then sorting and merging them.
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        Dict={}
        for index,char in enumerate(S):
            Dict.setdefault(char,[])
            Dict[char].append(index)
        interval=[]
        for key,val in Dict.items():
            interval.append([val[0],val[-1]])
        interval.sort()
        temp=interval[0]
        merge=[]
        for i in range(1,len(interval)):
            if temp[1]<interval[i][0]:
                merge.append(temp)
                temp=interval[i]
            else:
                temp[1]=max(temp[1],interval[i][1])
        merge.append(temp)
        return [j-i+1 for i,j in merge]
