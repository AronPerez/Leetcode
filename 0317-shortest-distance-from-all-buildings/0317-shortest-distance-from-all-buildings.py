class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # For each 1, start a BFS
            # When we final 0 cell, increase distance by + 1 based on steps already taken
        
        numOfHouses = distances = 0
        rows, cols = len(grid), len(grid[0])
        distances = [[[0,0] for _ in range(cols)] for _ in range(rows)]
        
        def bfs(row, col):
            nonlocal numOfHouses
            nonlocal distances
            distanceSum = currentHouseCount = 0
            queue = deque([(row, col, 0)])
            visited = set()
            
            while queue:
                row, col, step = queue.popleft()
                
                # Check if we reached a house 
                if grid[row][col] == 0: # Is a house
                    distances[row][col][0] += step
                    distances[row][col][1] += 1
                
                # Go left, right, up, down
                for dR, dC in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nR = dR + row
                    nC = dC + col
                    
                    if 0 <= nR < rows and 0 <= nC < cols: # In bounds
                        # Ensure we have not visited before
                        # Also ensure not obstacle
                        if (nR, nC) not in visited and grid[nR][nC] == 0:
                            visited.add((nR, nC))                            
                            queue.append((nR, nC, step+1))
        
        
                
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1: 
                    numOfHouses += 1
                    bfs(row, col)
                            
        minDistance = float('inf')
        for row in range(rows):
            for col in range(cols):
                if distances[row][col][1] == numOfHouses:
                    minDistance = min(minDistance,  distances[row][col][0])
                     
                    
                    
        return minDistance if minDistance != float('inf') else -1
        
        
        
        
        