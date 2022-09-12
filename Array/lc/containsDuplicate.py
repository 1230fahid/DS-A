class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        self.dict = {}
        for i in nums:
            if i in self.dict.keys():
                return True
            else:
                self.dict[i] = 1
                
        return False
