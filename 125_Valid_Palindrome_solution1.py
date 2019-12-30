class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal=[]
        for i in s:
            if i.isalpha() or i.isdigit():
                pal.append(i.lower())
        for i in range(len(pal)):
            if pal[i]!=pal[len(pal)-i-1]:
                return False
        return True
