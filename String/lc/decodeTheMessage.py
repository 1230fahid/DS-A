class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        num = 97
        self.dict = {}
        for i in key:
            if(len(self.dict) == 26):
                break
            if i in self.dict.keys() or i == " ":
                pass
            else:
                self.dict[i] = chr(num)
                num += 1
        
        newmessage = ""
        for i in message:
            if(i == " "):
                newmessage += " "
            else:
                newmessage += self.dict[i]
        #print(self.dict)
        return newmessage
