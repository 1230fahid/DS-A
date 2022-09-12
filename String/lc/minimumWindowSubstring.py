class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = {}
        sDict = {}
        test = {}
        num = 0
        
        for i in range(0, len(t)):
            if t[i] in tDict.keys():
                tDict[t[i]] += 1
            else:
                tDict[t[i]] = 1
                
        
        newstr = ""
        start = 0
        num = 0
        mins = len(s) + 1
        
        for i in range(0, len(s)):
            newstr += s[i]
            #num = 0
            if s[i] in tDict.keys():
                if(s[i] in sDict.keys()):
                    sDict[s[i]] += 1
                else:
                    sDict[s[i]] = 1
                
                if(len(tDict) == len(sDict)):
                    num = 0
                    for key in tDict.keys():
                        if sDict[key] >= tDict[key]:
                            num += 1
                            
                    if(num == len(tDict)):
                        if(len(newstr) < mins):
                            mins = len(newstr)
                            if(mins == len(t)):
                                return newstr
                        test[mins] = newstr
                        start = i + 1
                        break
                
        
        if(len(tDict) != len(sDict)):
            return ""
        
        #Once we find intial window, we shrink until we aren't equal
        for j in range(start, len(s)):
            while(len(newstr) != 0):
                num = 0
                if(len(tDict) == len(sDict)):
                    for key in tDict.keys():
                        if sDict[key] >= tDict[key]:
                            num += 1
                            
                    if(num != len(tDict)):
                        break
                    
                    if(len(newstr) < mins):
                        mins = len(newstr)
                        if(mins == len(t)):
                            return newstr
                        test[mins] = newstr
                    
                    
                    first = newstr[0]
                    newstr = newstr[1:len(newstr)]
                    if(first in sDict.keys()):
                        sDict[first] -= 1       
                        if(sDict[first] == 0):
                            del sDict[first]
                else:
                    break
            
            newstr += s[j]
            if(s[j] in tDict.keys()):
                if(s[j] in sDict.keys()):
                    sDict[s[j]] += 1
                else:
                    sDict[s[j]] = 1
                    
        
        
        while(len(newstr) != 0):
            num = 0
            if(len(tDict) == len(sDict)):
                    
                for key in tDict.keys():
                    if sDict[key] >= tDict[key]:
                        num += 1
                            
                if(num != len(tDict)):
                    break
                    
                if(len(newstr) < mins):
                    mins = len(newstr)
                    if(mins == len(t)):
                        return newstr
                    test[mins] = newstr
                        
                first = newstr[0]
                newstr = newstr[1:len(newstr)]
                if(first in sDict.keys()):
                    sDict[first] -= 1                        
                    if(sDict[first] == 0):
                        del sDict[first]
            else:
                break
            
        
        if(len(test) == 0):
            return ""
        return test[mins]  
