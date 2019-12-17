#mono stack
#time complexity O(n)

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res=[0 for _ in range(len(T))]
        stack=[]
        for i in range(len(res)):
            while stack and T[stack[-1]]<T[i]:
                day=stack.pop()
                res[day]=i-day
            stack.append(i)
        return res
