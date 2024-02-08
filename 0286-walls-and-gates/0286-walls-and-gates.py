class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # 2147483647 is empty
        # -1 wall or obstacle
        # 0 is gate
        
        if not rooms:
            return

        rowsCount = len(rooms)
        colsCount = len(rooms[0])
        
        # Find all the gates
        queue = deque()
        for r in range(rowsCount):
            for c in range(colsCount):
                if rooms[r][c] == 0: # If we find a gate, append its rol and col value
                    queue.append((r, c))
        
        
        # Using BFS, go from the gates
        INF = 2147483647
        
        while queue:
            row, col = queue.popleft()
            # Look left, right, down, up
            for directionRow, directionCol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                adjacentRow, adjacentCol = row + directionRow, col + directionCol
                if 0 <= adjacentRow < rowsCount and 0 <= adjacentCol < colsCount and rooms[adjacentRow][adjacentCol] == INF:    
                    rooms[adjacentRow][adjacentCol] = rooms[row][col] + 1
                    queue.append((adjacentRow, adjacentCol))
                    
                    
        
        