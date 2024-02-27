class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        
        rowCounter = Counter(tuple(row) for row in grid)
        
        for col in range(n):
            col = [grid[i][col] for i in range(n)]
            count += rowCounter[tuple(col)]
            
            
        return count