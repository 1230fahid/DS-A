class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        for i in range(1, len(strs)):
            newpref = ""
            mins = min(len(strs[i]), len(pref))
            for j in range(0, mins):
                if(pref[j] == strs[i][j]):
                    newpref += strs[i][j]
                else:
                    break
            pref = newpref
        
        return pref 
