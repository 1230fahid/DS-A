class Trie:

    def __init__(self):
        self.dict = {}
    def insert(self, word: str) -> None:
        self.dict[word] = 1

    def search(self, word: str) -> bool:
        if word in self.dict.keys():
            return True
        else:
            return False
    def startsWith(self, prefix: str) -> bool:
        for i in self.dict.keys():
            if len(i) >= len(prefix):
                if i[0: len(prefix)] == prefix:
                    return True
        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
