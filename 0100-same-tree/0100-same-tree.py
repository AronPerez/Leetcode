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
            p, q = queue.popleft()
            
            if p and q and p.val == q.val: # Must check if vals are equal
                queue.append((p.left, q.left))  # We need to check left next level 
                queue.append((p.right, q.right))  # We need to check left next level 
            elif p or q:
                return False
            
        return True
                
            