class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # # We wil alwaus have an island
        rows, cols = len(grid), len(grid[0]) # Gives us amount of rows and cols
        numOfIsland = 0
        visited = set()

        def dfs(row: int, col: int) -> None:
            # nonlocal visited
            # check if we are out of bounds and we have not visited
            if (row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0" or (row, col) in visited):
                return 

            # We need to know we have visited
            visited.add((row, col)) # {(0,0)}/ {(0,0), (0, 1))}/{(0,0), (0, 1)), (1,1)}/ {(0,0), (0, 1)), (1,1), (0,1)}
            # visited[row][col] = True

            # left, right, up, down
            dfs(row-1, col) # ob/in seen/1/ob
            dfs(row+1, col) # 1/is 0/inseen/0
            dfs(row, col+1) # ob/inseen/inSeen/ob
            dfs(row, col-1) # 1/0/0/inSeen
            # if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited:


        for row in range(rows): # 0
            for col in range(cols): # 0
                if grid[row][col] == '1' and (row, col) not in visited: # true,
                    dfs(row, col)
                    numOfIsland += 1 # 1


        return numOfIsland # 1