class Solution:
    def firstUniqChar(self, s: str) -> int:
        wordDict = {}
        for i in s:
            if i in wordDict.keys():
                wordDict[i] += 1
            else:
                wordDict[i] = 1
        
        a = 0
        for key in wordDict.keys():
            if wordDict[key] == 1:
                a = 1
                break
        
        if(a == 0):
            return -1
        
        return s.index(key)
