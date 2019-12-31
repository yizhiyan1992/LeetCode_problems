# clock problem is like circular array
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time=[]
        for t in timePoints:
            hour,minute=t.split(':')
            time.append(int(hour)*60+int(minute))
        time.sort()
        res=float('inf')
        for i in range(1,len(time)):
            temp=min(time[i]-time[i-1],24*60-(time[i]-time[i-1]))
            if temp<res:
                res=temp
        if min(time[-1]-time[0],24*60-(time[-1]-time[0]))<res:
            res=min(time[-1]-time[0],24*60-(time[-1]-time[0]))
        return res
