class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left=max(weights)
        right=sum(weights)
        self.res=right
        def BS(left,right):
            if left>right: return
            middle=left+(right-left)//2
            day=D
            cur_sum=0
            for weight in weights:
                # here, the logic is that the sum of weight must not exceed the capacity. So in each for-loop, we need to first check if the weight is over the capacity by adding the item. if yes, we need to use a new container for this package.
                if cur_sum+weight>middle:
                    day-=1
                    cur_sum=0
                cur_sum+=weight
            # need to watch that is the last container is empty! If the last one after iteration is not empty, we need to minus 1!
            if cur_sum>0:
                day-=1
            if day>=0:
                self.res=min(self.res,middle)
                BS(left,middle-1)
            else:
                BS(middle+1,right)
            return
        BS(left,right)
        return self.res
