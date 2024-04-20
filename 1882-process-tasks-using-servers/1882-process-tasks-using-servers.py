class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
        servers[i] = weight
        
        heapq: min-heap that allows us to efficiently extract the server with the lowest weight
        
        1. availableServers = [(weight, index), ...]
        2. heapify availableServers (min heap) so 
        3. unavailableServers = [] holds unavailable servers

        4. go through tasks, looking at index for t and duration for how long it takes
            make sure we dont process tasks before they arrive
            Since server assignment is dependant on the current time
            
            when processing availableServers, we only consider servers that have finished their task by current time
            lets us only assign servers to tasks that are free at the moment
            servers that are still busy with pervious task are skipped until available
            
            5.  Repeatedly check if any servers in unavailableServers have finished their tasks
                5a. Remove finished servers from unavailableServers
                5b. Add the freed server back to availableServers
                
            6. if we have available servers
                6a. Retrieve the most suitable free server (lowest weight, lowest index).
                6b. Mark this server as busy by adding it to unavailableServers, along with its calculated finish time.
                8c. then append to answer list
            7. else no servers available
                7a. Since all servers are busy, directly take the next server to be freed from unavailableServers
                7b. Update its finish time with the new task (time + taskDuration) and add it back to unavailableServers
                7c. add server to answer
                
        8. return ans
        """
        
        ans = []
        availableServers = [(w, i) for i, w in enumerate(servers)]                              # 1
        heapq.heapify(availableServers)                                                         # 2
        unavailableServers = []                                                                 # 3
        
        for time, taskDuration in enumerate(tasks):                                             # 4
            
            while unavailableServers and unavailableServers[0][0] <= time:                      # 5               
                _, weight, serverIndex = heapq.heappop(unavailableServers)                      # 5a
                heapq.heappush(availableServers, (weight, serverIndex))                         # 5b
                
            if availableServers:                                                                # 6
                weight, serverIndex = heapq.heappop(availableServers)                           # 6a
                heapq.heappush(unavailableServers, (time + taskDuration, weight, serverIndex))  # 6b
                ans.append(serverIndex)                                                         # 6c
            else:                                                                               # 7
                finishTime, weight, serverIndex = heapq.heappop(unavailableServers)             # 7a
                heapq.heappush(unavailableServers, (finishTime + taskDuration, weight, serverIndex))  # 7b
                ans.append(serverIndex)                                                         # 7c
                
        return ans                                                                              # 8
                
            
            