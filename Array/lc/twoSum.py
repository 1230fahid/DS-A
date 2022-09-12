class Solution:
    def twoSum_my_solution(self, nums: List[int], target: int) -> List[int]:
        tup = tuple(nums)
        j = 0
        val = 0
        for i in range(0, len(nums)):
            val = target - nums[i]
            j += 1
            tup = tup[1:]
            #print(tup)
            if val in tup:
                num = tup.index(val)
                return i, num + j
        return None
    def two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
        if(len(nums) < 2):
            return None
        if(len(nums) == 2):
            if((nums[0] + nums[1]) == target):
                return [0,1]
            else:
                return None
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i , j]
        return None
    def two_sum_optimal(self, nums: List[int], target: int) -> List[int]:   #[0,2,4,6], 8
        lookup = {}                                                   
        for cnt, num in enumerate(nums): #{0:0, 1:2, 2:4, 3:6}
            if target - num in lookup:
                return lookup[target-num], cnt #lookup[8-6]=lookup[2]=1, cnt = 3
            lookup[num] = cnt   #{0:0, 2:1, 4:2}
