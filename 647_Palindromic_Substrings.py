#palindrome problem.
class Solution:
    def countSubstrings(self, s: str) -> int:
        palin={}
        for i in range(len(s)):
            left=i-1;right=i+1
            palin[(i,i)]=1
            while left>=0 and right<=len(s)-1 and s[left]==s[right]:
                palin[(left,right)]=1
                left-=1;right+=1
            left=i;right=i+1
            while left>=0 and right<=len(s)-1 and s[left]==s[right]:
                palin[(left,right)]=1
                left-=1;right+=1
        return len(palin)
