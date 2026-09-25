class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_1d = [i for s in matrix for i in s]
        low = 0
        high = len(matrix_1d) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix_1d[mid] == target:
                return True
            elif matrix_1d[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False