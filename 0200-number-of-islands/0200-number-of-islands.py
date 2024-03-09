class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # # We wil alwaus have an island
        rows, cols = len(grid), len(grid[0]) # Gives us amount of rows and cols
        numOfIsland = 0
        
        def dfs(row: int, col: int) -> None:
            # check if we are out of bounds and we have not visited
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":

                grid[row][col] = "0"

                dfs(row-1, col)
                dfs(row+1, col)
                dfs(row, col+1)
                dfs(row, col-1)
            else: # Out of bounds
                return


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    numOfIsland += 1

 
        return numOfIsland # 1
        