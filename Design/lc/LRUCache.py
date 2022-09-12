class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.track = {}
        self.num = 0
    def get(self, key: int) -> int:
        if(key in self.dict.keys()):
            del self.track[key]
            self.track[key] = 1
            return self.dict[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if(key in self.dict.keys()):
            del self.track[key]
            self.dict[key] = value
            self.track[key] = value
        else:
            if(self.num == self.capacity):
                for i in self.track.keys():
                    break
                #print("i is",i)
                del self.track[i]
                del self.dict[i]
                self.track[key] = value
                self.dict[key] = value
            else:
                self.track[key] = value
                self.dict[key] = value
                self.num+=1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
