#palindrome problem. Use the idea of symmetry! we can fix a pivot everytime and search the longest substring by spreading out from both sides.
# Time compleixty: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        max_pal=s[0]
        for i in range(len(s)):
            temp=s[i]
            #case1
            mid=i;left=mid-1;right=mid+1
            while left>=0 and right<=len(s)-1:
                if s[left]==s[right]:
                    temp=s[left]+temp+s[right]
                    left-=1;right+=1
                else: break
                if len(temp)>len(max_pal):
                    max_pal=temp
            #case2
            temp=''
            left=i;right=i+1
            while left>=0 and right<=len(s)-1:
                if s[left]==s[right]:
                    temp=s[left]+temp+s[right]
                    left-=1;right+=1
                else: break
                if len(temp)>len(max_pal):
                    max_pal=temp
        return max_pal
