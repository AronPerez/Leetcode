# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSum = float('-inf')
        
        def dfs(node: Optional[TreeNode]):
            nonlocal maxPathSum
            if node is None: # We are done, we have reached a leaf
                return 0
            
            # if negative we ignore and set to 0 to not mess up sum
            left = max(dfs(node.left), 0) # Read the left
            right = max(dfs(node.right), 0) # Read the right

            currentMaxPathSum = node.val + left + right # Read parent and its children
            maxPathSum = max(maxPathSum, currentMaxPathSum) # Keep track of largest path so far

            return node.val + max(left, right) # Go back up stack and choose the max or children
    
        dfs(root)
        
        return maxPathSum