class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            row_seen= set()
            for i in range(9):
                if board[row][i]=='.':
                    continue
                if board[row][i] in row_seen:
                    return False

                row_seen.add(board[row][i])

        for col in range(9):
            col_seen= set()
            for i in range(9):
                if board[i][col]=='.':
                    continue
                if board[i][col] in col_seen:
                    return False

                col_seen.add(board[i][col])

        for square in range(9):
            square_seen= set()
            for i in range(3):
                for j in range(3):
                    row= (square//3) * 3 + i
                    col= (square % 3) * 3 + j
                    if board[row][col]=='.':
                        continue
                    if board[row][col] in square_seen:
                        return False
                    square_seen.add(board[row][col])
        return True




