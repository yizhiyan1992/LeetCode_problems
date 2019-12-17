#solution 2: DP
#We can think this problem in this way: each interger and be added or minus (+/-), is there a combination of all elements s.t. the sum=0?
# Dp[i][j]=True if using the first i elements can constitude value j
# check if Dp[n][0]=True
# the size of this array is proportional to the product of elements len and sum.
# Instead of using array, we can use a hash table to store the values
# time complexity: O(Sum*n) 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        max_number=max(nums)
        n=len(nums)
        Dict={}
        Dict[0]=1
        for i in nums:
            temp={}
            for index,value in Dict.items():
                temp[index+i]=1
                temp[index-i]=1
            Dict=temp
        if 0 in Dict:
            return True
        else:
            return False
