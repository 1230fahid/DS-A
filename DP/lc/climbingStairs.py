class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1 or n == 2):
            return n
        arr = [0] * (n+1)
        m=0
        self.climb(n, arr, m)
        return arr[len(arr)-1]
    
    def climb(self, n, arr, m):
        if(n<0):
            return 0
        if(n == 0):
            m+=1
            return m
        #elif(n < 0):
        #    return -1
        if (arr[n] == 0):
            arr[n] = self.climb(n-1, arr,m) + self.climb(n-2, arr,m)
        return arr[n]
