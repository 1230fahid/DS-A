class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        chars = {}
        for i in range(0, len(s)):
            if s[i] in chars.keys():
                chars[s[i]].append(i)
            else:
                chars[s[i]] = [i]
        
        for i in range(0, len(distance)):
            if chr(i + 97) in chars.keys():
                letter = chr(i + 97)
                first = chars[letter][0]
                second = chars[letter][1]
                if(second - first-1) != distance[i]:
                    return False
        
        return True
