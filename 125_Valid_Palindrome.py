#two pointers, time complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        pt1=0
        pt2=len(s)-1
        while pt1<=pt2:
            # pt1<=len(s)-1 , because it may out of index
            while pt1<=len(s)-1 and not (s[pt1].isdigit() or s[pt1].isalpha()):
                pt1+=1
            while pt2>=0 and not (s[pt2].isdigit() or s[pt2].isalpha()):
                pt2-=1
            # this is for the corner cases that there might be no alphanumeric characters in the str.
            if pt1<=pt2:
                if s[pt1].lower()!=s[pt2].lower():
                    return False
            pt1+=1
            pt2-=1
        return True
