# Easy , use binary heap. Time complexity: O(nlogn) space complexity: O(1)

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=list(map(lambda i:-i,stones))
        heapq.heapify(stones)
        while len(stones)>1:
            rock1=-heapq.heappop(stones)
            rock2=-heapq.heappop(stones)
            if rock1-rock2!=0:
                heapq.heappush(stones,rock2-rock1)
        if len(stones)==1:
            return -stones[0]
        else:
            return 0
