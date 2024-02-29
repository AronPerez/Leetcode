class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # (2,2) 2-1 + 2 - 2 = 1
        # (0,0) abs(0-1) + abs(0-2) = 3
        
        # Basically we need to pick the house thats closest to another house
        # (0,0)/(2,2) -> ()
        
        # BFS from each empty cell
        # Each next sell is 1 distancce further
        
        # Need a way to keep track of the num of houses we have reached from empty cell
        """
            Empty Land to Houses
            
            numOfHouses = 0
            
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 1: 
                        numOfHouses += 1
            minDistance = float('inf')
            
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 0: # Start BFS
                    
            return minDistance if minDistance != float('inf') else -1
        """
      
        # Will need to assert that the empty cell BFS has reached n numOfHouses
        # Once we reach a house, we take our distance and add it to a currentSum
        # Basically that current sum will use min
        # If we cannot reach all houses from empty cell, then that cell cannot be used
            # We'd need to update all cells visited to 2, basically making it an obstacle so we do not waste time there
        # And we would update a minDistance sum if we reached all houses
        
        numOfHouses = 0
        rows, cols = len(grid), len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1: 
                    numOfHouses += 1
       
        def bfs(row, col, numOfHouses):
            distanceSum = currentHouseCount = 0
            queue = deque([(row, col, 0)])
            visited = set()
            
            while queue:
                row, col, step = queue.popleft()
                
                # Check if we reached a house 
                if grid[row][col] == 1: # Is a house
                    distanceSum += step
                    currentHouseCount += 1
                    continue
                
                # Go left, right, up, down
                for dR, dC in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nR = dR + row
                    nC = dC + col
                    
                    if 0 <= nR < rows and 0 <= nC < cols: # In bounds
                        # Ensure we have not visited before
                        # Also ensure not obstacle
                        if (nR, nC) not in visited and grid[nR][nC] != 2:
                            visited.add((nR, nC))                            
                            queue.append((nR, nC, step+1))
            
            # We did not reach all houses
            if currentHouseCount != numOfHouses: 
                for row in range(rows):
                    for col in range(cols):
                        if grid[row][col] == 0 and (row, col) in visited: # Set as bound
                            grid[row][col] = 2
                            
                return float('inf')
            
            # Reached all houses
            return distanceSum
                            
        minDistance = float('inf')
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    minDistance = min(minDistance,  bfs(row, col, numOfHouses))
                    
                    
        return minDistance if minDistance != float('inf') else -1
        
        
        
        
        