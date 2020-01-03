'''
stack problem
First thought: can we use recursion?
Because the len(str)<=100, and there is no way to do prunning and DP, so we cannot use recursion for this problem.

Though2: Use stack.
create two stacks PAR and STAR to store '(' and '*' seperately.
There are two conditions that '*' cannot help, namely *( and )*
when we find a ')'
1) pop PAR to counteract it;
2) if PAR is empty, pop STAR (because * can be '('.
3) If both empty, return False

After we finish the for-loop, we need to check if the stack PAR is empty or not.
If the stack is not empty, then we continuously do while-iteration for stack PAR.
1) pop PAR and pop STAR everytime, if '('_position>'*'_position, return False
2) If STAR is empty, return False

Finally, return True
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        par=[]
        star=[]
        for i,j in enumerate(s):
            if j=='*':
                star.append([j,i])
            elif j=='(':
                par.append([j,i])
            else:
                if not par:
                    if not star:
                        return False
                    else:
                        star.pop()
                else:
                    par.pop()
        while par:
            if not star: return False
            if par[-1][1]>star[-1][1]:
                return False
            else:
                par.pop()
                star.pop()
        return True
