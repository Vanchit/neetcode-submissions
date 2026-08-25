class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        
        left = 0
        right = rows * columns - 1

        while left <= right:
            mid =(left + right) // 2
            #Keep in mind row and column    
            row = mid // columns
            column = mid % columns

            middle_value = matrix[row][column]

            if middle_value == target:
                return True
            elif middle_value < target:
                left = mid +1
            else:
                right = mid -1 
        return False
    