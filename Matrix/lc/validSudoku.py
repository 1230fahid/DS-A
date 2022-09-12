##I know i can do this problem easier if i just create more dictionaries in and use them in the first two for loops. I'm not gonna, but uh I probably could do that
class Solution:
    def subboard(self, begin_row, end_row, begin_col, end_col, board):
        mydict = {}
        for i in range(begin_row, end_row):
            for j in range(begin_col, end_col):
                if(board[i][j] == '.'):
                    continue
                elif board[i][j] not in mydict.keys():
                    mydict[board[i][j]] = 0
                else:
                    return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.dict1 = {}
        
        for i in range(0, 9):
            for j in range(0,9):
                if(board[i][j] == '.'):
                    continue
                if board[i][j] not in self.dict1.keys():
                    self.dict1[board[i][j]] = 0
                else:
                    return False
            self.dict1 = {}
        
        for j in range(0, 9):
            for i in range(0,9):
                if(board[i][j] == '.'):
                    continue
                if board[i][j] not in self.dict1.keys():
                    self.dict1[board[i][j]] = 0
                else:
                    return False
            self.dict1 = {}
        
        begin_row = 0
        end_row = 3
        begin_col = 0
        end_col = 3
        for i in range(0, 3):
            begin_col = 0
            end_col = 3
            for j in range(0, 3):
                if self.subboard(begin_row, end_row, begin_col, end_col, board) == False:
                    print(begin_row, end_row)
                    return False
                begin_col += 3
                end_col += 3
                
            begin_row += 3
            end_row += 3
            
        return True
        
