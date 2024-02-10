class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid2)
        cols = len(grid2[0])
        count = 0
        
        @cache
        def dfs(row, col):
            nonlocal valid
            # Make sure we are not out of bounds and are looking at a 1
            if 0 <= row < rows and 0 <= col < cols and grid2[row][col] == 1:
                # mark where we've been
                grid2[row][col] = "X"
                # Check if are corresponding with grid1
                if grid1[row][col] == 0:
                    valid = False
                    
                # Look left, right, up, down
                dfs(row-1, col)
                dfs(row+1, col)
                dfs(row, col+1)
                dfs(row, col-1)

        for row in range(rows):
            for col in range(cols):
                valid = True
                if grid2[row][col] == 1: # We found an island, search
                    dfs(row, col)
                    if valid: # We foudn a subisland
                        count += 1
                        
        return count