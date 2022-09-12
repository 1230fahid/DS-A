#Had to use both hints
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        changeX = 0; changeY = 0; direction = 1
        for i in range(len(instructions)):
            if(instructions[i] == "G"):
                if(direction == 0):
                    changeX += 1
                elif(direction == 1):
                    changeY += 1
                elif(direction == 2):
                    changeX -= 1
                elif(direction == 3):
                    changeY -= 1
                
            elif(instructions[i] == "L"):
                if(direction == 0):
                    direction = 1
                elif(direction == 1):
                    direction = 2
                elif(direction == 2):
                    direction = 3
                elif(direction == 3):
                    direction = 0
                    
            elif(instructions[i] == "R"):
                if(direction == 0):
                    direction = 3
                elif(direction == 1):
                    direction = 0
                elif(direction == 2):
                    direction = 1
                elif(direction == 3):
                    direction = 2
        
        
        
        
        if(changeX == 0 and changeY == 0) or (direction != 1):
            return True
        else:
            return False
        
        
