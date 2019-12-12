#Bucket sort problem
#Because we know the maximum Manhatton distance is 2000. So we can set the bucket number as 2000.
#Time complexity: O(MN)

#If using binary heap for this problem, the time complexity would be O(NMlog(MN)), time exceeds!
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        if not workers or not bikes: return []
        Bucket=[[] for _ in range(2001)]
        for j in range(len(workers)):
            for i in range(len(bikes)):
                Bucket[abs(bikes[i][0]-workers[j][0])+abs(bikes[i][1]-workers[j][1])].append([i,j])
        Workers=[False for _ in range(len(workers))]
        Bikes=[False for _ in range(len(bikes))]
        ans=[None for _ in range(len(workers))]
        for i in Bucket:
            for j in i:
                if Bikes[j[0]]==False and Workers[j[1]]==False:
                    Bikes[j[0]]=True
                    Workers[j[1]]=True
                    ans[j[1]]=j[0]

        return ans
