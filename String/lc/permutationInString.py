class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
        lookup = {}
        lookup2 = {}
        for i in range(len(s1)):
            if s1[i] in lookup.keys():
                lookup[s1[i]] +=1
            else:
                lookup[s1[i]] = 1
            if s2[i] in lookup2.keys():
                lookup2[s2[i]] +=1
            else:
                lookup2[s2[i]] = 1
        num = 0
        for key in lookup2.keys():
            if key in lookup.keys() and lookup[key] == lookup2[key] :
                num += 1
        if num == len(lookup):
            return True
        else:
            num = 0
        
        for k in range(len(s1), len(s2)):
            if(s2[k] in lookup2.keys()):
                lookup2[s2[k]] += 1
            else:
                lookup2[s2[k]] = 1
            lookup2[s2[k-len(s1)]] -= 1
            for key in lookup2.keys():
                if key in lookup.keys() and lookup[key] == lookup2[key] :
                    num += 1
            if num == len(lookup):
                return True
            else:
                num = 0
            
        return False
