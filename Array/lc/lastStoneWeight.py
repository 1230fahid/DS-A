class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while(len(stones) != 1):
            x = stones[len(stones)-2]
            y = stones[len(stones)-1]
            stones.pop(len(stones)-2)
            stones[len(stones)-1] -= x
            stones.sort()
        return stones[0]
