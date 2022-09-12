class WordDictionary:

    def __init__(self):
        self.dict = {}
        #self.dict2 = {}
        self.words = []

    def addWord(self, word: str) -> None:
        self.dict[word] = 1
        #self.dict2[word] = 1
        
    def search(self, word: str) -> bool:
        if("." not in word):
            if(word in self.dict.keys()):
                return True
            else:
                return False
        else:
            dots = []

            for i in self.dict.keys():
                if(len(word) != len(i)):
                    continue
                num = 0
                for j in range(0, len(i)):
                    if(i[j] == word[j]) or (word[j] == "."):
                        num += 1
                if(num == len(word)):
                    return True
            return False
                    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
