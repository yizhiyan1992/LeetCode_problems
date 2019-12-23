#solve by priority Q.
#Store [element,frequncy] in the dict.
#Build the max priority q based on frequency for each element. (the build-in heapq is a min-pq)
#Go through the PQ n+1 times for every iteration.
# pop the max element and minus 1. If the frequency is larger than 1, save it in the temp array (because for each iteration, an element can be only used once)
# If PQ is empty before n+1 for-loop, break in advance
# case1: if PQ is not empty, then add counter by n+1
# case2: if PQ is empty, but temp is not empty (now we need idle to be inserted into those empty space), then add counter by n+1
# case3: if PQ is empty, and temp is also empty, add counter by temp_count, and return the result.
# Time complecity: O(nlogn) , it's a little bit slower than the first solution.
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        Dict={}
        for i in tasks:
            Dict.setdefault(i,0)
            Dict[i]+=1
        PQ=[]
        for i,j in Dict.items():
            PQ.append([-j,i]) # because heapq is min-pq
        heapq.heapify(PQ)
        temp=[]
        counter=0
        while True:
            temp_count=0
            for i in range(n+1):
                if not PQ: break
                cur_times,cur_task=heapq.heappop(PQ)
                temp_count+=1
                if cur_times<-1:
                    temp.append([cur_times+1,cur_task])
            if PQ:
                counter+=n+1
            elif not PQ:
                if temp:
                    counter+=n+1
                else:
                    counter+=temp_count
                    return counter
            while temp:
                heapq.heappush(PQ,temp.pop())
