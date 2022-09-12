class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        p = 0
        i = 0
        l = list(s)
        while(i < len(l)):
            print(i)
            if(i+1 >= len(l)):
                p = 1
            
            if s[i] =="M":
                num+=1000
            elif(s[i] == "C"):
                if(i+1 == len(s)):
                    num += 100
                elif(s[i+1] == "M"):
                    num+=900
                    i+=1
                elif(s[i+1] == "D"):
                    num+=400
                    i+=1
                else:
                    num+=100
            elif(s[i] == "D"):
                num+=500
            elif(s[i] == "X"):
                if(i+1 == len(s)):
                    num += 10
                elif(s[i+1] == "L"):
                    num+=40
                    i+=1
                elif(s[i+1] == "C" ):
                    num+=90
                    i+=1
                else:
                    num+=10
            elif(s[i] == "L"):
                num+=50
            elif(s[i] == "I"):
                if(i+1 == len(s)):
                    num += 1
                elif(s[i+1] == "X"):
                    num+=9
                    i+=1
                elif(s[i+1] == "V"):
                    num+=4
                    i+=1
                else:
                    num+=1
            elif(s[i] == "V"):
                num+=5
            i+=1
        print(num)
        return(num)
                
