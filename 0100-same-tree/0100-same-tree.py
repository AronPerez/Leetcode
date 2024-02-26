# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(q, p)])

        
        while queue:
            tree1, tree2 = queue.popleft()
            
            if tree1 is None and tree2 is None:
                continue
            elif tree1 is None:
                return False
            elif tree2 is None:
                return False
            
            if tree1.val != tree2.val: # Must check if vals are equal
                return False
            
            
            queue.append((tree1.left, tree2.left))  # We need to check left next level 
            queue.append((tree1.right, tree2.right))  # We need to check left next level 
            
        return True
                
            