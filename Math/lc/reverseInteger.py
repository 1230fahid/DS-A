class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = x[::-1]
        if(x[len(x)-1] == "-"):
            x = x[len(x)-1] + x[0:len(x)-1]
        x = int(x)
        if(x > 2**31 - 1) or (x <-(2**31)):
            x=0
        return x
