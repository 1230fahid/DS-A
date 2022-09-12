class Solution:
    ##This has soooo many cases. Really consider edge cases man
    def myAtoi(self, s: str) -> int:
        if(len(s) > 200):
            return
        num = 0
        inc = ""
        a = list(s)
        i = 0
        sign = 0
        if(len(a) == 0):
            return 0
        if(len(a) == 1):
            if(a[0].isnumeric()):
                num = int(a[0])
                return num
            else:
                return 0
        while(a[i].isnumeric() == False):
            if(a[i] != ' '):
                if(a[i] == '+' or a[i] == '-') and (a[i+1].isnumeric() and i+1 < len(a)):
                    break
                else:
                    return 0
            else:
                i += 1
                if(i >= len(a)):
                    return 0
        print(i)
        sign = 1
        if(a[i] == '+'):
            sign = 1
            a = a[i+1:]
        elif(a[i] == '-'):
            sign = -1
            a = a[i+1:]
        else:
            a = a[i:]
        j = 0
        print(a)
        print(len(a))
        print()
        while(a[j].isnumeric() == True and j<=len(a)-1):
            inc += a[j]
            print(j)
            print(inc)
            j+=1
            if(j >= len(a)):
                break
        
        num = int(inc)
        print()
        print(num)
        num = num * sign
        if(num < -2147483648):
            num = -2147483648
        elif(num > 2147483647):
            num = 2147483647
        print(num)
        return num
