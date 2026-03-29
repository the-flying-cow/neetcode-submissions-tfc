class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_h= 0, len(matrix)-1
        

        while row_l <= row_h:
            row_m= row_l + (row_h - row_l)//2
            
            if target <  matrix[row_m][0]:
                row_h= row_m - 1

            elif target >  matrix[row_m][len(matrix[0]) - 1]:
                row_l= row_m + 1
            
            else:
                col_l, col_h= 0, len(matrix[0]) - 1
                while col_l <= col_h:

                    col_m= col_l + (col_h - col_l)//2

                    if matrix[row_m][col_m] == target:
                        return True
                    
                    elif target > matrix[row_m][col_m]:
                        col_l= col_m + 1
                    else:
                        col_h= col_m - 1

                return False

        return False