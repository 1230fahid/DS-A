class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""
        i = 1
        while(num != 0):
            n = num%10 * i
            i *= 10
            if(n >= 1 and n < 10):
                if(n == 1):
                    s += "I"
                elif(n == 2):
                    s += "II"
                elif(n == 3):
                    s += "III"
                elif(n == 4):
                    s += "VI"
                elif(n == 5):
                    s += "V"
                elif(n == 6):
                    s += "IV"
                elif(n == 7):
                    s += "IIV"
                elif(n == 8):
                    s += "IIIV"
                elif(n == 9):
                    s += "XI"
            elif(n >=10 and n < 100):
                if(n == 10):
                    s += "X"
                elif(n == 20):
                    s += "XX"
                elif(n == 30):
                    s += "XXX"
                elif(n == 40):
                    s += "LX"
                elif(n == 50):
                    s += "L"
                elif(n == 60):
                    s += "XL"
                elif(n == 70):
                    s += "XXL"
                elif(n == 80):
                    s += "XXXL"
                elif(n == 90):
                    s += "CX"
            elif(n >= 100 and n < 1000):
                if(n == 100):
                    s += "C"
                elif(n == 200):
                    s += "CC"
                elif(n == 300):
                    s += "CCC"
                elif(n == 400):
                    s += "DC"
                elif(n == 500):
                    s += "D"
                elif(n == 600):
                    s += "CD"
                elif(n == 700):
                    s += "CCD"
                elif(n == 800):
                    s += "CCCD"
                elif(n == 900):
                    s += "MC"
            elif(n >= 1000):
                if(n == 1000):
                    s += "M"
                elif(n == 2000):
                    s += "MM"
                elif(n == 3000):
                    s += "MMM"
            num = num//10
        
        return s[::-1]
