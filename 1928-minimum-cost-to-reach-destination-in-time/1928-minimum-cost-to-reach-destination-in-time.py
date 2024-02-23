class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        # x_i = city1
        # y_y = city2 
        # time_i = time
        
        # cost of journey is the sum of passingFees
        # what is the min cost to complete the journey?
        
        # City 0 cost is 5
        # City 1 cost is 1
        
        # Start at city 0
        
        # Want to reach a city in maxTime <= mins
        
        # The min value I need to assign it maxTime
        
        # DFS where I go from the node in city1
        # I get its cost to go to city2
        # I also store its time to see if the meets the requirements of a min city
        
            # Recurse to node that city2 is in
            # Repeat the process
            # Once I get the a city that has no other refs where it is x_i, I know I am done
            
        # Build our graph
        graph = self.build_graph(edges)
        n = len(passingFees)

        start_state = (passingFees[0], 0, 0)  # (cost, time, city)
        heap = [start_state]
        visited = set()

        while heap:
            cost, time, city = heapq.heappop(heap)

            if city == n - 1:
                return cost

            if (city, time) in visited:
                continue  # Already visited with a better cost or time
            visited.add((city, time))

            for neighbor, travel_time in graph[city]:
                new_cost = cost + passingFees[neighbor]
                new_time = time + travel_time
                if new_time <= maxTime:
                    heapq.heappush(heap, (new_cost, new_time, neighbor))

        return -1  # Couldn't reach the destination
    
    def build_graph(self, edges):
        graph = defaultdict(list)
        for city1, city2, time in edges:
            graph[city1].append((city2, time))
            graph[city2].append((city1, time))  # Bidirectional
        return graph
        
        
        