class Solution:
    def isHappy(self, n: int) -> bool:
        if(n == 1):
            return True
        i = 0
        summ = 0
        
        while(1):
            summ = 0
            while(n != 0):
                i = n%10
                n = n//10
                summ = summ + (i**2)
            if (summ == 1):
                return True
            else:
                n = summ
                if(n < 10):
                    if(n == 7):
                        return True
                    else:
                        return False
            #break
            
        #return False
