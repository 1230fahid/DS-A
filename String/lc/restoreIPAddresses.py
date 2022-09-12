class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if(len(s) > 12 or len(s) < 4):
            return

        valids = {}
        quads0 = ""
        quads1 = ""
        quads2 = ""
        iteration = 1
        if(len(s) <= 10):
            self.ip(s, 0, 1, valids, iteration, quads0 + s[0:1] + '.')
            self.ip(s, 0, 2, valids, iteration, quads1 + s[0:2] + '.')
            self.ip(s, 0, 3, valids, iteration, quads2 + s[0:3] + '.')
        elif(len(s) == 11):
            self.ip(s, 0, 2, valids, iteration, quads1 + s[0:2] + '.')
            self.ip(s, 0, 3, valids, iteration, quads2 + s[0:3] + '.')
        elif(len(s) == 12):
            self.ip(s, 0, 3, valids, iteration, quads2 + s[0:3] + '.')
        
        l = []
        for i in valids.keys():
            l.append(i)
        #print(l)
        return l
        
    def ip(self, s, begin, end, valids, iteration, quads):
        #print("quads0 is",quads)
        if(iteration == 5):
            if(begin != len(s)):
                return
            else:
                if quads[0:len(quads)-2] in valids.keys():
                    return
                valids[quads[0:len(quads)-2]] = 1
                return
        if(begin >= len(s)):
            return
        if s[begin] == "0" and ((end - begin) != 1):
            return
        num = int(s[begin:end])
        if(num > 255):
            return
        self.ip(s, end, end+1, valids, iteration+1, quads + s[end:end+1] + '.')
        self.ip(s, end, end+2, valids, iteration+1, quads + s[end:end+2] + '.')
        self.ip(s, end, end+3, valids, iteration+1, quads + s[end:end+3] + '.')
