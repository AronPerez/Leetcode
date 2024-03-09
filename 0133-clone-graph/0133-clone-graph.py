"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Base cases
        if not node:
            return node

        ans = {}
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        ans[node] = Node(node.val, [])

        # BFS
        while queue:
            currentNode = queue.popleft()
            # Go through all neighbors
            for child in currentNode.neighbors: # is Node class
                if child not in ans: # Haven't seen before, enqueue
                    ans[child] = Node(child.val, []) # Clone the neighbor and put in the visited, if not present already
                    queue.append(child) # We will process later
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                ans[currentNode].neighbors.append(ans[child])
                
        return ans[node]
                
                    
                    
                
        