class Solution:    
    def fib(self, n: int) -> int:
        if(n == 0 or n == 1):
            return n
        if(n == 2):
            return 1
        
        fibonacci = [0] * (n+1)
        fibonacci[1] = 1
        fibonacci[2] = 1
        
        for i in range(2,n+1):
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
        
        return fibonacci[len(fibonacci)-1]
