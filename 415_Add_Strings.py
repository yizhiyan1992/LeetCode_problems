class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_r=num1[::-1]
        num2_r=num2[::-1]
        temp=[0 for _ in range(max(len(num1),len(num2))+1)]
        res=[0 for _ in range(max(len(num1),len(num2))+1)]
        for i in range(len(res)):
            dig1=0;dig2=0
            if i<=len(num1_r)-1:
                dig1=int(num1_r[i])
            if i<=len(num2_r)-1:
                dig2=int(num2_r[i])
            dig_sum=dig1+dig2+temp[i]
            if len(str(dig_sum))==2:
                temp[i+1]+=1
                res[i]=str(dig_sum)[1]
            else:
                res[i]=str(dig_sum)
        res.reverse()
        if res[0]=='0':
            return ''.join(res[1:])
        else:
            return ''.join(res)
