class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows, cols= len(board), len(board[0])

        # check in rows

        for i in range(rows):

            seen= set()

            for j in range(cols):

                if board[i][j] in seen and board[i][j] != ".":
                    return False
                seen.add(board[i][j])

        # check in cols    
        for i in range(cols):

            seen= set()

            for j in range(rows):
                
                if board[j][i] in seen and board[j][i] != ".":
                    return False
                seen.add(board[j][i])
        
        # check in square boxes

        for box in range(9):
            
            seen= set()

            for i in range(3):
                for j in range(3):

                    r= (box // 3) * 3 + i
                    c= (box % 3) * 3 + j

                    if board[r][c] == ".":
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
                    
        return True
