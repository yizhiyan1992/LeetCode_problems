class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res=[0 for _ in range(len(num1)+len(num2)+2)]
        num1_lis=list(num1);num1_lis.reverse()
        num2_lis=list(num2);num2_lis.reverse()
        for j in range(len(num1_lis)):
            temp=[0 for _ in range(len(num1)+len(num2)+2)]
            for i in range(len(num2_lis)):
                product=int(num1_lis[j])*int(num2_lis[i])
                #be careful about assigning values
                if product>=10:
                    temp[i+j]+=int(str(product)[1])
                    temp[i+j+1]+=int(str(product)[0])
                else:
                    temp[i+j]+=product
            for k in range(len(temp)):
                dig_sum=res[k]+temp[k]
                if dig_sum>=10:
                    res[k]=int(str(dig_sum)[1])
                    res[k+1] += int(str(dig_sum)[0])
                else:
                    res[k]=dig_sum
        res.reverse()
        #corner case, if the product is zero
        if_zero=0
        for i in res:
            if_zero+=int(i)
        if if_zero==0:
            return '0'
        while res[0]==0:
            del res[0]
        return ''.join(list(map(str,res)))
