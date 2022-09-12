class Solution:
    def compress(self, chars: List[str]) -> int:
        if(len(chars) == 1):
            return 1
        lookup = {}
        prev = chars[0]
        lookup[prev] = 1
        i = 1
        while (i < len(chars)):
            if chars[i] == prev:
                lookup[prev] += 1
                chars.pop(i)
            else:
                if(lookup[prev] == 1):
                    prev = chars[i]
                    i+=1
                    lookup[prev]=1
                else:
                    freq=lookup[prev]
                    if freq<10:
                        chars.insert(i, str(freq))
                        i+=1
                        prev=chars[i]
                        lookup[prev]=1
                        i+=1
                    else:
                        freq=lookup[prev]
                        for j in str(freq):
                            chars.insert(i, j)
                            i+=1
                        prev=chars[i]
                        lookup[prev]=1
                        i+=1
                    
        if(lookup[prev] != 1):
            for j in str(lookup[prev]):
                chars.insert(i, j)
                i+=1
        return(len(chars))
