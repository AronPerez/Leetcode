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
            
        graph = defaultdict(list)
        
        for u, v, t in edges:
            graph[u].append((v,t))
            graph[v].append((u,t))
            
        n = len(passingFees)
        
        fees = [sys.maxsize] * n
        times = [maxTime] * n
        fees[0] = passingFees[0]
        times[0] = 0
        
        priorityQueue = [(passingFees[0], 0, 0)] # Fee, time, node
        
        while priorityQueue:
            fee, time, u = heappop(priorityQueue)
            
            for (v, t) in graph[u]: # for node2 and time, how do we improve?
                if time+t <= maxTime and (fee+passingFees[v] < fees[v] or time+t < times[v]): # If we can make improvement
                    heappush(priorityQueue, (fee+passingFees[v], time+t, v))
                    if fee+passingFees[v] < fees[v]:
                        fees[v] = fee+passingFees[v]
                    if time+t < times[v]:
                        times[v] = time+t
                        
        return fees[-1] if fees[-1] < sys.maxsize else -1
        
        
        