#use binary search to maintain the LIS, where the time complexity is O(nlogn)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        def Binarysearch(num,size,LIS,left,right):
            if left>right:
                return
            middle=left+(right-left)//2
            if num<=LIS[middle]:
                if middle==0:
                    LIS[0]=num
                    return size
                elif num>LIS[middle-1]:
                    LIS[middle]=num
                    return size
                else:
                    size=Binarysearch(num,size,LIS,left,middle-1)
            else:
                if middle==size-1:
                    LIS.append(num)
                    size+=1
                    return size
                else:
                    size=Binarysearch(num,size,LIS,middle+1,right)
            return size

        n=len(nums)
        size=0
        LIS=[]
        for num in nums:
            if LIS==[]:
                LIS.append(num)
                size+=1
                continue
            size=Binarysearch(num,size,LIS,0,len(LIS))
        return size
