class Solution:
    def addBinary(self, a: str, b: str) -> str:
    
        exp = 0
        num1 = 0
        i = -1
        while (i > -len(a)-1):
            num1 += int(a[i]) * (2**exp)
            exp+=1
            i-=1
        
        exp = 0
        num2 = 0
        i = -1
        while (i > -len(b)-1):
            num2 += int(b[i]) * (2**exp)
            exp+=1
            i-=1
            
        sum = num1+num2
        summ=""
        if(sum == 0):
            return str(sum)
        else:
            while(sum != 0):
                rm = sum%2
                summ += str(rm)
                sum=sum//2
            summ = summ[::-1]
            return summ
