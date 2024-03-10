class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Define the possible directions: right, left, down, up

        def isValid(x, y):
            return 0 <= x < n and 0 <= y < n  # Check if the coordinates (x, y) are within the grid boundaries

        # Create a priority queue (min-heap) to store the squares to be visited
        pq = [(grid[0][0], 0, 0)]  # (elevation, x, y)
        visited = set([(0, 0)])  # Keep track of visited squares
        max_elevation = 0  # Track the maximum elevation encountered so far

        while pq:
            elevation, x, y = heapq.heappop(pq)  # Get the square with the lowest elevation from the priority queue
            max_elevation = max(max_elevation, elevation)  # Update the maximum elevation encountered

            if (x, y) == (n - 1, n - 1):  # If we have reached the bottom-right square
                return max_elevation  # Return the maximum elevation (least time) required to reach the bottom-right square

            for dx, dy in directions:  # Explore the adjacent squares
                nx, ny = x + dx, y + dy  # Calculate the new coordinates
                if isValid(nx, ny) and (nx, ny) not in visited:  # If the new coordinates are valid and not visited
                    visited.add((nx, ny))  # Mark the square as visited
                    heapq.heappush(pq, (grid[nx][ny], nx, ny))  # Add the square to the priority queue

        return 0  # If the bottom-right square is not reachable, return 0
        