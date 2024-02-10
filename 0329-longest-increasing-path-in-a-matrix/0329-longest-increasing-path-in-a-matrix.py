class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longestPath = 0 
        rows, cols = len(matrix), len(matrix[0])
        
        @cache
        def dfs(row, col):
            currentPath = 1
            # Go left, right, up, down
            for dR, dC in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                # We need to ensure we dont go out of bounds
                # We only need to consider values in cells larger than itself
                if 0 <= row + dR < rows and 0 <= col + dC < cols and matrix[row+dR][col+dC] > matrix[row][col]:
                    currentPath = max(currentPath, 1 + dfs(row+dR, col+dC))
             
            # Need to return the max value
            return currentPath
        
        
        for row in range(rows):
            for col in range(cols):
                longestPath = max(longestPath, dfs(row, col))
                
                
        return longestPath