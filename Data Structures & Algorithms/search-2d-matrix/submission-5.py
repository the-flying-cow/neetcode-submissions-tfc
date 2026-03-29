class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m= len(matrix)
        n= len(matrix[0])

        low_rows= 0
        high_rows= m-1


        while low_rows <= high_rows:
            mid_rows= low_rows + (high_rows - low_rows)//2

            if target < matrix[mid_rows][0]:
                high_rows= mid_rows - 1
            elif target > matrix[mid_rows][n-1]:
                low_rows= mid_rows + 1
            else:
                low_cols= 0
                high_cols= n-1

                while low_cols <= high_cols:
                    mid_cols= low_cols + (high_cols - low_cols)//2

                    if target == matrix[mid_rows][mid_cols]:
                        return True
                    elif target > matrix[mid_rows][mid_cols]:
                
                        low_cols= mid_cols + 1
                    else:
                        high_cols= mid_cols - 1

                return False

        return False