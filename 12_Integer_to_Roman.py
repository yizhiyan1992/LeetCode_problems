class Solution:
    def intToRoman(self, num: int) -> str:
        res=''
        div,mod=divmod(num,1000)
        if div!=0:
            res+='M'*(div)
            num=mod
        div,mod=divmod(num,100)
        if div!=0:
            if div==4:
                res+='CD'
            elif div==9:
                res+='CM'
            elif div<4:
                res+='C'*(num//100)
            else:
                res+='D'+'C'*(num//100-5)
            num=mod
        div,mod=divmod(num,10)
        if div!=0:
            if div==4:
                res+='XL'
            elif div==9:
                res+='XC'
            elif div<4:
                res+='X'*(num//10)
            else:
                res+='L'+'X'*(num//10-5)
            num=mod
        if num==4:
            res+='IV'
        elif num==9:
            res+='IX'
        elif num<4:
            res+='I'*num
        else:
            res+='V'+'I'*(num-5)
        return res
