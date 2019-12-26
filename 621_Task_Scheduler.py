# find the most frequent element, name the frequency as F
# the lower bound is (F-1)*(n-1)+R, where n is the interval given by the question already and R is the number of remaining elements.
# R=the number of elements with the hightest frequency. For example, AAABBB R=2, AAABBCCD. R=1
# Be careful that this is only the lower bound, once the length of tasks is longer than the lower bound, other elements can be set meeting the requirement.
# So we need to compare the lower bound and the length of the task to return the max val.
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        Dict={}
        for i in tasks:
            Dict.setdefault(i,0)
            Dict[i]+=1
        Max=max(Dict.values())
        counter=0
        for i in Dict.values():
            if i==Max:
                counter+=1
        res=(Max-1)*(n+1)+counter
        return res if res>len(tasks) else len(tasks)
