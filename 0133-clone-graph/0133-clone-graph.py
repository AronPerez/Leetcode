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
        visited = {}
        
        def dfs(node: Optional['Node']):
            nonlocal visited
            # Base cases
            if not node:
                return node
            
            # If the node was already visited before.
            # Return the clone from the visited dictionary.
            if node in visited:
                return visited[node]
            
            # Create a clone for the given node.
            # Note that we don't have cloned neighbors as of now, hence [].
            clone_node = Node(node.val, [])
            
            # The key is original node and value being the clone node.
            visited[node] = clone_node
            
            # Iterate through the neighbors to generate their clones
            # and prepare a list of cloned neighbors to be added to the cloned node.
            if node.neighbors:
                clone_node.neighbors = [dfs(n) for n in node.neighbors]

            return clone_node
                
        return dfs(node)
                
                    
                    
                
        