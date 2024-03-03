class Solution:
    def __init__(self):
        self.islandId = -1
        self.islandAreas = {}
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def largestIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        
       # Go thr 2nd time, flip each 1 to get the max area
        def dfs(row, col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                grid[row][col] = self.islandId
                
                area = 1
                
                for rD, rC in self.directions:
                    area += dfs(row + rD, col + rC)
                    
                return area
            else:
                return 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    islandArea = dfs(row, col)
   
                    self.islandAreas[self.islandId] = islandArea
                    self.islandId -= 1
                    
        maxArea = 0
        
     
        
        for row in range(rows):
            for col in range(cols):
                if not grid[row][col]:
                    area = 1
                    surrounding = set()
                    
                    for rD, rC in self.directions:
                        nR, nC = row + rD, col + rC
                        
                        if 0 <= nR < rows and 0 <= nC < cols and grid[nR][nC] != 0:
                            surrounding.add(grid[nR][nC])
                            
                    for islandId in surrounding:
                        area += self.islandAreas[islandId]
                    
                    maxArea = max(maxArea, area)
                    
        return maxArea if maxArea else len(grid) ** 2
    
                            
                    
                    
        
        