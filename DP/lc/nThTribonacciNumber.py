class Solution:
    def tribonacci(self, n: int) -> int:
        F = []
        num = 0
        F.insert(0,0)
        F.insert(1,1)
        F.insert(2,1)
        for i in range(3, n+1):
            num = F[i-3] + F[i-2] + F[i-1]
            F.insert(i,num)
        return F[n]
