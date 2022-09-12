class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if(num1 == "0" or num2 == "0"):
            return "0"
        newnum1 = 0
        newnum2 = 0
        
        for i in num1:
            if i == "0":
                newnum1 = (10 * newnum1) + 0
            elif i == "1":
                newnum1 = (10 * newnum1) + 1
            elif i == "2":
                newnum1 = (10 * newnum1) + 2
            elif i == "3":
                newnum1 = (10 * newnum1) + 3
            elif i == "4":
                newnum1 = (10 * newnum1) + 4
            elif i == "5":
                newnum1 = (10 * newnum1) + 5
            elif i == "6":
                newnum1 = (10 * newnum1) + 6
            elif i == "7":
                newnum1 = (10 * newnum1) + 7
            elif i == "8":
                newnum1 = (10 * newnum1) + 8
            elif i == "9":
                newnum1 = (10 * newnum1) + 9
            
        for i in num2:
            if i == "0":
                newnum2 = (10 * newnum2) + 0
            elif i == "1":
                newnum2 = (10 * newnum2) + 1
            elif i == "2":
                newnum2 = (10 * newnum2) + 2
            elif i == "3":
                newnum2 = (10 * newnum2) + 3
            elif i == "4":
                newnum2 = (10 * newnum2) + 4
            elif i == "5":
                newnum2 = (10 * newnum2) + 5
            elif i == "6":
                newnum2 = (10 * newnum2) + 6
            elif i == "7":
                newnum2 = (10 * newnum2) + 7
            elif i == "8":
                newnum2 = (10 * newnum2) + 8
            elif i == "9":
                newnum2 = (10 * newnum2) + 9
        
        return str(newnum1 * newnum2)
