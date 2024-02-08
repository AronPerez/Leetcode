class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # mangattan distance = abs(x1 - x2) + abs(y1 - y2)
        
        # (3 - x) + (4 - y)
        
        # some kinda min index
        # Some kinda min calc
        # Iterate point through points
        # If point[0] == x or point[1] == y
        # We perform calc
        # Get the min of calc and eventually 
        
        minIndex = -1
        shortestDistance = float('inf')
        
        
        for coordinates in points:
            if coordinates[0] == x or coordinates[1] == y:
                manhattanDistance = abs(x - coordinates[0]) + abs(y - coordinates[1])
                if manhattanDistance < shortestDistance: # We know to update the value since less than old
                    minIndex = points.index(coordinates) # Gives index of element
                    shortestDistance = manhattanDistance
        
        return minIndex