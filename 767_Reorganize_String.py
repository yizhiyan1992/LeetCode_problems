'''
 priority queue problem
 First, we need to cnsider if the string that meets the requirement exist. If the most frequent element is larger than len(S)/2, then it must not exist.
 Second, how to build the proposed string?
 Condition1: two consecutive characters must not be the same
 Condition2: The elements with higher frequency should be used more frequenly
 Con1+Con2----> use priority queue!
 '''
import heapq
import math
class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S: return ''
        Dict={}
        for char in S:
            Dict.setdefault(char,0)
            Dict[char]+=1
        max_char=max(Dict.values())
        if max_char>math.ceil(len(S)/2):
            return ''
        res=''
        #min heap queue
        PQ=[(-j,i) for (i,j) in Dict.items()]
        heapq.heapify(PQ)
        while PQ:
            # temp array is to store the elements that popped out but overllapped with S[-1]. Need to push back to the queue.
            temp=[]
            while True:
                fre,char=heapq.heappop(PQ)
                if res and res[-1]==char:
                    temp.append((fre,char))
                else:
                    res=res+char
                    fre+=1
                    if fre!=0:
                        temp.append((fre,char))
                    break
            while temp:
                heapq.heappush(PQ,temp.pop())
        return res
