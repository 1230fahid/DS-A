class Solution:
    def isValid(self, s: str) -> bool:
        op = ('(','{','[')
        cl = (')','}',']')
        stack = []
        for i in s:
            if i in op:
                stack.append(i)
            elif i in cl:
                if(len(stack) == 0):
                    return False
                if i == cl[0]:
                    if stack[len(stack)-1] == op[0]:
                        stack.pop()
                    else:
                        return False
                if i == cl[1]:
                    if stack[len(stack)-1] == op[1]:
                        stack.pop()
                    else:
                        return False
                if i == cl[2]:
                    if stack[len(stack)-1] == op[2]:
                        stack.pop()
                    else:
                        return False
            else:
                return False
            
        if len(stack) == 0:
            return True
            
